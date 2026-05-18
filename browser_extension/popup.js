const analyseBtn = document.getElementById("analyseBtn");
const loading = document.getElementById("loading");
const resultBox = document.getElementById("resultBox");
const errorBox = document.getElementById("errorBox");

const predictionText = document.getElementById("predictionText");
const confidenceText = document.getElementById("confidenceText");
const riskText = document.getElementById("riskText");
const alertText = document.getElementById("alertText");

const reportBtn = document.getElementById("reportBtn");
const reportBox = document.getElementById("reportBox");
const explainText = document.getElementById("explainText");
const featureList = document.getElementById("featureList");

analyseBtn.addEventListener("click", async () => {
  loading.classList.remove("hidden");
  resultBox.classList.add("hidden");
  errorBox.classList.add("hidden");
  reportBox.classList.add("hidden");
  reportBtn.classList.add("hidden");

  try {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

    const [{ result }] = await chrome.scripting.executeScript({
      target: { tabId: tab.id },
      func: () => {
        return {
          url: window.location.href,
          html: document.body.innerText,
          domain: window.location.hostname
        };
      }
    });

    const response = await fetch("http://127.0.0.1:5000/api/analyse", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        url: result.url,
        html: result.html,
        domain: result.domain
      })
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.error || "Analysis failed");
    }

    resultBox.classList.remove("safe", "danger");

    if (data.result === "legitimate") {
      predictionText.textContent = "Prediction: Safe";
      riskText.textContent = "Low Risk";
      alertText.textContent =
        "No significant phishing indicators detected. This website appears safe.";
      resultBox.classList.add("safe");
    } else {
      predictionText.textContent = "Prediction: High Risk";
      riskText.textContent = "High Risk";
      alertText.textContent =
        "This page shows patterns associated with AI-generated phishing. Proceed with caution.";
      resultBox.classList.add("danger");
    }

    confidenceText.textContent = data.confidence + "%";

    explainText.textContent =
      "Explainability Score: " + data.explain_score + " — " + data.explain_label;

    featureList.innerHTML = "";

    data.feature_report.forEach(item => {
      const row = document.createElement("div");
      row.className = "feature-row";

      let riskClass = "risk-low";

      if (item.risk === "Medium") {
        riskClass = "risk-medium";
      }

      if (item.risk === "High") {
        riskClass = "risk-high";
      }

      row.innerHTML = `
        <strong>${item.feature}</strong>
        <span>${item.description}</span><br>
        <span>Value: ${item.value}</span><br>
        <span class="${riskClass}">Risk: ${item.risk}</span>
      `;

      featureList.appendChild(row);
    });

    reportBtn.textContent = "View Detailed Report";
    reportBtn.classList.remove("hidden");
    resultBox.classList.remove("hidden");

  } catch (error) {
    errorBox.textContent = error.message;
    errorBox.classList.remove("hidden");
  } finally {
    loading.classList.add("hidden");
  }
});

reportBtn.addEventListener("click", () => {
  reportBox.classList.toggle("hidden");

  if (reportBox.classList.contains("hidden")) {
    reportBtn.textContent = "View Detailed Report";
  } else {
    reportBtn.textContent = "Hide Detailed Report";
  }
});