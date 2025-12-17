<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>House Price Predictor</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body class="bg-light">
    <div class="container mt-5">
        <div class="card p-4 shadow-lg">
            <h2 class="text-center mb-4">🏡 House Price Prediction</h2>
            <form id="predictForm">
                <div class="mb-3">
                    <label class="form-label">Area (sq ft)</label>
                    <input type="number" id="area" class="form-control" required>
                </div>
                <div class="mb-3">
                    <label class="form-label">Bedrooms</label>
                    <input type="number" id="bedrooms" class="form-control" required>
                </div>
                <div class="mb-3">
                    <label class="form-label">Bathrooms</label>
                    <input type="number" id="bathrooms" class="form-control" required>
                </div>
                <button class="btn btn-primary w-100" type="submit">Predict Price</button>
            </form>
            <h4 class="mt-4 text-center" id="result"></h4>
        </div>
    </div>

<script>
    document.getElementById("predictForm").addEventListener("submit", async function(e){
        e.preventDefault();

        const data = {
            area: parseFloat(document.getElementById("area").value),
            bedrooms: parseInt(document.getElementById("bedrooms").value),
            bathrooms: parseInt(document.getElementById("bathrooms").value)
        };

        const response = await fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        document.getElementById("result").innerText = `Predicted Price: $${result.predicted_price}`;
    });
</script>

</body>
</html>
