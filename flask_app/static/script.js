// according to https://developers.google.com/youtube/iframe_api_reference we need to add some js to get this working.

const checkbox = document.getElementById("checkbox");
const content = document.getElementById("content");
const contentText = document.getElementById("contentText");
const checkboxDefault = document.getElementById("checkboxDefault");

checkbox.addEventListener("change", () => {
  if (checkbox.checked) {
    checkboxDefault.disabled = "true";
    checkbox.value = "1";
    content.innerText = "Link:";
    contentText.rows = "1";
  } else {
    checkboxDefault.disabled = "false";
    content.innerText = "Content:";
    contentText.rows = "4";
  }
});
