const API_BASE = "http://127.0.0.1:8000";

const documentFile = document.getElementById("documentFile");
const fileName = document.getElementById("fileName");
const documentText = document.getElementById("documentText");
const sampleBtn = document.getElementById("sampleBtn");
const analyzeBtn = document.getElementById("analyzeBtn");
const statusBox = document.getElementById("statusBox");
const errorBox = document.getElementById("errorBox");

const summaryOutput = document.getElementById("summaryOutput");
const orgList = document.getElementById("orgList");
const dateList = document.getElementById("dateList");
const amountList = document.getElementById("amountList");
const invoiceList = document.getElementById("invoiceList");
const riskList = document.getElementById("riskList");
const actionList = document.getElementById("actionList");
const confidenceScore = document.getElementById("confidenceScore");

const tabButtons = document.querySelectorAll(".tab-btn");
const tabPanels = document.querySelectorAll(".tab-panel");

let currentTab = "text";

const SAMPLE_TEXT =
  "Vendor agreement between Blue Harbour Consulting and Rivergate Foods. " +
  "Service term runs from 1 April 2026 to 31 March 2027 with a monthly retainer of $7,500. " +
  "Invoice INV-20431 is due within 15 days. Late payment may trigger penalty and escalation. " +
  "Breach of service levels can result in termination and liability review.";

tabButtons.forEach((btn) => {
  btn.addEventListener("click", () => {
    const tab = btn.getAttribute("data-tab");
    if (!tab) return;

    tabButtons.forEach((button) => button.classList.remove("active"));
    btn.classList.add("active");

    tabPanels.forEach((panel) => panel.classList.remove("active"));
    document.getElementById(`${tab}-panel`).classList.add("active");

    currentTab = tab;
    documentFile.value = "";
    documentText.value = "";
    fileName.textContent = "No file selected";
    setStatus("Ready for analysis.");
    setError("");
  });
});

documentFile.addEventListener("change", (event) => {
  const file = event.target.files[0];
  fileName.textContent = file ? file.name : "No file selected";
  if (file) {
    setError("");
    setStatus(`Selected file: ${file.name}`);
  }
});

sampleBtn.addEventListener("click", () => {
  documentText.value = SAMPLE_TEXT;
  documentText.focus();
  setError("");
  setStatus("Sample text inserted. Click Analyze Document to run the review.");
});

function setError(message) {
  errorBox.hidden = !message;
  errorBox.textContent = message || "";
}

function setStatus(message) {
  statusBox.textContent = message;
}

function setLoading(isLoading) {
  analyzeBtn.disabled = isLoading;
  analyzeBtn.classList.toggle("is-loading", isLoading);
}

function renderChips(container, items) {
  if (!Array.isArray(items) || items.length === 0) {
    container.innerHTML = '<span class="chip empty">None detected</span>';
    return;
  }
  container.innerHTML = items.map((item) => `<span class="chip">${escapeHtml(item)}</span>`).join("");
}

function renderList(container, items) {
  if (!Array.isArray(items) || items.length === 0) {
    container.innerHTML = '<li class="empty">None detected.</li>';
    return;
  }
  container.innerHTML = items.map((item) => `<li>${escapeHtml(item)}</li>`).join("");
}

function renderResults(data) {
  summaryOutput.textContent = data.summary || "No summary returned.";
  renderChips(orgList, data.key_entities?.organizations || []);
  renderChips(dateList, data.key_entities?.dates || []);
  renderChips(amountList, data.key_entities?.amounts || []);
  renderChips(invoiceList, data.key_entities?.invoice_ids || []);
  renderList(riskList, data.risk_flags || []);
  renderList(actionList, data.action_items || []);
  confidenceScore.textContent = data.confidence_score || "Medium";
}

function escapeHtml(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

analyzeBtn.addEventListener("click", async () => {
  setError("");

  if (currentTab === "file") {
    const file = documentFile.files[0];
    if (!file) {
      setError("Please choose a .txt file to upload.");
      return;
    }

    setLoading(true);
    setStatus("Uploading document and analyzing content...");

    try {
      const formData = new FormData();
      formData.append("file", file);

      const response = await fetch(`${API_BASE}/upload-document`, {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail || `Request failed with status ${response.status}`);
      }

      const data = await response.json();
      renderResults(data);
      setStatus("Analysis complete.");
    } catch (error) {
      const message = error instanceof Error ? error.message : "An unknown error occurred.";
      setError(`Analysis failed: ${message}`);
      setStatus("Unable to complete analysis.");
    } finally {
      setLoading(false);
    }
    return;
  }

  const text = documentText.value.trim();
  if (!text) {
    setError("Please paste document text to analyze.");
    return;
  }

  setLoading(true);
  setStatus("Analyzing document text...");

  try {
    const response = await fetch(`${API_BASE}/analyze-text`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text }),
    });

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.detail || `Request failed with status ${response.status}`);
    }

    const data = await response.json();
    renderResults(data);
    setStatus("Analysis complete.");
  } catch (error) {
    const message = error instanceof Error ? error.message : "An unknown error occurred.";
    setError(`Analysis failed: ${message}`);
    setStatus("Unable to complete analysis.");
  } finally {
    setLoading(false);
  }
});
