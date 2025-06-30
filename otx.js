
fetch("https://otx.alienvault.com/api/v1/pulses/?limit=5")
  .then(response => response.json())
  .then(data => {
    const headlines = data.results.map(p => p.name).join(" • ");
    document.getElementById("ticker").innerText = headlines;
  })
  .catch(error => {
    console.error('Failed to load feed:', error);
    document.getElementById("ticker").innerText = "Threat feed unavailable.";
  });
