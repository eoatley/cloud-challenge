async function incrementAndSetVisitors() {
  const response = await fetch(
    "https://ymd01arws4.execute-api.us-east-1.amazonaws.com/update-visitors-dynamodb",
    {
      method: "POST",
    }
  );
  const text = await response.text();

  document.getElementById("count").innerHTML = text;
}

incrementAndSetVisitors();
