document.getElementById('add-team-member').addEventListener('click', function() {
    let name = prompt('Enter team member name:');
    let role = prompt('Enter team member role:');
    if (name && role) {
        addTeamMember(name, role);
    }
});

function addTeamMember(name, role) {
    let table = document.getElementById('team-table').getElementsByTagName('tbody')[0];
    let newRow = table.insertRow();

    let cell1 = newRow.insertCell(0);
    let cell2 = newRow.insertCell(1);
    let cell3 = newRow.insertCell(2);

    cell1.textContent = name;
    cell2.textContent = role;

    let removeButton = document.createElement('button');
    removeButton.textContent = 'Remove';
    removeButton.addEventListener('click', function() {
        table.removeChild(newRow);
    });
    cell3.appendChild(removeButton);
}

document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault();
    alert('Message sent successfully!');
});