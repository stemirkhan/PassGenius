function copy(copy_space) {
  let textarea = document.getElementById(copy_space);
  textarea.select();
  document.execCommand("copy");
}