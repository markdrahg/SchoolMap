
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('load-schools-button').addEventListener('click', function() {
        console.log("FETCH 1");

        const selectedCountryValue = document.getElementById('interestCountry').value;
        const selectedAcceptanceRate = document.getElementById('acceptanceRate').value;

        // Map the selected value to the corresponding data
        const countryMap = {
            '1': 'USA',
            '2': 'Canada',
            '3': 'Germany'
        };

        const acceptanceRateMap = {
            '1': 'Low',
            '2': 'Medium',
            '3': 'High'
        };

        // Map the selected value to the corresponding field name
        const selectedCountry = countryMap[selectedCountryValue];
        const selectedAcceptance = acceptanceRateMap[selectedAcceptanceRate];

        fetch('/api/schools/')
            .then(response => response.json())
            .then(data => {
                let table = document.getElementById('schools');
                
                if (table) {
                    table.innerHTML = '';
                    let filteredschool1;
                    let filteredschool2;

                    if (selectedCountryValue === "All" || !selectedCountry) {
                        filteredschool1 = data; // Show all books if "All" is selected
                    } else {
                        filteredschool1 = data.filter(School => School.country === selectedCountry);
                    }

                    if (selectedAcceptanceRate === "All" || !selectedAcceptance) {
                        filteredschool2 = filteredschool1; // Show all books if "All" is selected
                    } else if (selectedAcceptance == 'Low') {
                        filteredschool2 = filteredschool1.filter(School => School.acceptance_rate < '39.00');
                    } else if (selectedAcceptance == 'Medium') {
                        filteredschool2 = filteredschool1.filter(School => (School.acceptance_rate < '69.00') && (School.acceptance_rate > '38.00'));
                    } else {
                        filteredschool2 = filteredschool1.filter(School => School.acceptance_rate > '68');
                    }

                    filteredschool2.forEach(school => {
                        let row = document.createElement('tr');
                        row.innerHTML = `
                            <td><input type="checkbox" class="save-checkbox" data-school-id="${school.id}"></td>
                            <td>${school.name}</td>
                            <td>${school.country}</td>
                            <td>${school.acceptance_rate}</td>
                            <td><a href="${school.website}" target="_blank">${school.website}</a></td>
                        `;
                        table.appendChild(row);
                    });
                } else {
                    console.error('Element with ID "schools" not found.');
                }
            })
            .catch(error => console.error('Error fetching data:', error));
    });

    // Function to load and display saved schools
    function loadSavedSchools() {
        fetch('/api/saved_schools/')
            .then(response => response.json())
            .then(data => {
                let table = document.getElementById('stored_schools');
                
                if (table) {
                    table.innerHTML = `
                        <tr>
                            <th>DATA</th>
                        </tr>
                    `;

                    data.forEach(school => {
                        let row = document.createElement('tr');
                        row.innerHTML = `
                            <td><input type="checkbox" class="save-checkbox" data-school-id="${school.id}" checked></td>
                            <td>${school.name}</td>
                            <td>${school.acceptance_rate}</td>
                            <td>${school.country}</td>
                            <td><a href="${school.website}" target="_blank">${school.website}</a></td>
                        `;
                        table.appendChild(row);
                    });
                } else {
                    console.error('Element with ID "stored_schools" not found.');
                }
            })
            .catch(error => console.error('Error fetching saved schools:', error));
    }

    // Initial load of saved schools
    loadSavedSchools();



    // Event listener for checkbox changes
document.getElementById('schools').addEventListener('change', function(e) {
    if (e.target.classList.contains('save-checkbox')) {
        const schoolId = e.target.getAttribute('data-school-id');
        const isChecked = e.target.checked;

        if (!schoolId) {
            console.error('School ID is undefined');
            return;
        }

        console.log(`School ID: ${schoolId}, Is Checked: ${isChecked}`);

        fetch(isChecked ? '/save_school/' : '/unsave_school/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
            body: `school_id=${schoolId}`
        })
        .then(response => response.json())
        .then(data => {
            console.log(data.status);
            loadSavedSchools(); // Reload saved schools to reflect changes
        })
        .catch(error => console.error('Error:', error));
    }
});









    // document.getElementById('schools').addEventListener('change', function(e) {
    //     if (e.target.classList.contains('save-checkbox')) {
    //         const schoolId = e.target.getAttribute('data-school-id');
    //         const isChecked = e.target.checked;

    //         console.log(`School ID: ${schoolId}, Is Checked: ${isChecked}`);

    //         fetch(isChecked ? '/save_school/' : '/unsave_school/', {
    //             method: 'POST',
    //             headers: {
    //                 'Content-Type': 'application/x-www-form-urlencoded',
    //                 'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
    //             },
    //             body: `school_id=${schoolId}`
    //         })
    //         .then(response => response.json())
    //         .then(data => {
    //             console.log(data.status);
    //             loadSavedSchools(); // Reload saved schools to reflect changes
    //         })
    //         .catch(error => console.error('Error:', error));
    //     }
    // });
});



