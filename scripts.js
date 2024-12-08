function showAssignRole(userId) {
    const modal = document.getElementById('assign-role-modal');
    modal.style.display = 'block';

    const form = document.getElementById('assign-role-form');
    form.onsubmit = async (e) => {
        e.preventDefault();
        const roleId = document.getElementById('role-select').value;

        const response = await fetch('/assign_role/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: JSON.stringify({ user_id: userId, role_id: roleId }),
        });

        if (response.ok) {
            alert('Role assigned successfully!');
            modal.style.display = 'none';
        } else {
            alert('Error assigning role.');
        }
    };
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === `${name}=`) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
