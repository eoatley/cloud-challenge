async function incrementAndSetVisitors() {
  const response = await fetch(
    "https://ymd01arws4.execute-api.us-east-1.amazonaws.com/update-visitors-dynamodb",
    {
      method: "POST",
    }
  );
  const responseText = await response.text();
  const parsedResponse = JSON.parse(responseText);
  const newVisitors = parsedResponse.new_visitors;

  document.getElementById("count").innerHTML = newVisitors;
}

incrementAndSetVisitors();
