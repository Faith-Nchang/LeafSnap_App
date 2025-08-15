document.getElementById('uploadDiv').onclick = function() {
    document.getElementById('fileInput').click();
};

// replace <label> with file
document.getElementById('fileInput').addEventListener('change', function(e) {
    const label = document.getElementById('upload-label');
    if (this.files && this.files[0]) {
        label.innerHTML = `<p>added: ${this.files[0].name}</p>`;
    } else {
        label.innerHTML = '<p>Click to upload a leaf image</p>';
    }
});