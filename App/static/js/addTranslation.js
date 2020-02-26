onDOMContentLoaded = (function(){ 
    const radioOne = document.getElementById('source-0');
    const radioTwo = document.getElementById('source-1');
    const srcInput = document.getElementById('src');
    const srcLabel = document.getElementById('src-label');

    // An exception for the edit form

    if (radioTwo.checked) {
        srcInput.readOnly = false;
    }

    // General rules for both edit and add forms

    const radios = Array.from(document.querySelectorAll('#source li'));
    radios.forEach(el => el.addEventListener('change', () => {
        if (radioTwo.checked) {
            srcInput.readOnly = false;
            srcInput.placeholder = 'Enter source details here';
            srcLabel.classList.remove('text-muted');
        } else {
            srcInput.readOnly = true;
            srcInput.placeholder = '';
            srcInput.setAttribute('value', '');
            srcLabel.classList.add('text-muted');
        }
    }))
})()


