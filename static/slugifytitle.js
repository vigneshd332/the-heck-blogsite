const titleInput = document.querySelector("input[name='title']")
const slugInput = document.querySelector("input[name='slug']")
const slugifytitle = (val) =>{
    return val.toString().toLowerCase().trim()
      .replace(/&/g, '-and-')
      .replace(/[\s\W-]+/g, '-')
};

titleInput.addEventListener('keyup', (e) => {
    slugInput.setAttribute('value', slugifytitle(titleInput.value));
});