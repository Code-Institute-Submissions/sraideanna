// Handles the confirm dialogue for the delete button (only on street page)

onDOMContentLoaded = (function(){ 
	const deleteBtn = document.getElementById('delete-translation');
	if (deleteBtn) {
		deleteBtn.addEventListener('click', (e) => {
			if (!confirm('Are you sure you want to delete this translation?')) {
				e.preventDefault(); 
		   		e.stopPropagation();
			}
		});
	}  
})()



