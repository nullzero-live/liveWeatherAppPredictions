document.addEventListener("DOMContentLoaded", function() {
    // Get elements
    const startDate = document.getElementById("startDate");
    const endDate = document.getElementById("endDate");
    const predictButton = document.getElementById("predictButton");
    const outputBox = document.getElementById("outputBox");
  
    // Event listener for the predict button
    predictButton.addEventListener("click", async function() {
      const startDateValue = startDate.value;
      const endDateValue = endDate.value;
      if (startDateValue && endDateValue) {
        // Clear any previous output
        outputBox.textContent = "Processing...";
  
        try {
          // Make an API call to the FastAPI backend
          const response = await fetch("http://your_backend_url/predict", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              start_date: startDateValue,
              end_date: endDateValue,
            }),
          });
  
          if (response.status === 200) {
            const data = await response.json();
            outputBox.textContent = `Prediction: ${data.prediction}`;
          } else {
            outputBox.textContent = "Failed to get prediction.";
          }
        } catch (error) {
          console.error(error);
          outputBox.textContent = "An error occurred.😿";
        }
      } else {
        outputBox.textContent = "Please fill in both dates.";
      }
    });
  });
  