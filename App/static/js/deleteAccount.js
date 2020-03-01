// Handles the confirm dialogue for the delete button (only on street page)

onDOMContentLoaded = (function(){ 
	const deleteAccountBtn = document.getElementById('delete-account');
		deleteAccountBtn.addEventListener('click', (e) => {
			if (!confirm('Are you sure you want to delete your account? \n It cannot be retrieved.')) {
				e.preventDefault(); 
		   		e.stopPropagation();
			}
		});	
})();