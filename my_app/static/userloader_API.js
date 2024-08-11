
// document.getElementById('closeButton').addEventListener('click', function() {
//     document.getElementById('alertPopup').classList.add('hidden');
// });

// document.getElementById('okButton').addEventListener('click', function() {
//     document.getElementById('alertPopup').classList.add('hidden');
// });



document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('load-books-button').addEventListener('click', loadBooks);
});



function closspopUp() {
    document.getElementById('alertPopup').classList.add('hidden');
}

function loadBooks() {
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
    


    fetch('/books/json/')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('book-container');
            container.innerHTML = '';  // Clear previous content

            // Filter the data based on the selected country, unless "All" is selected
            let filteredBooks;
            let filteredBooks2;
            if (selectedCountryValue === "All" || !selectedCountry) {
                filteredBooks = data; // Show all books if "All" is selected
            } else {
                filteredBooks = data.filter(book => book.school.country === selectedCountry);
            }

            // Filter the data based on the selected acceptance - rate, unless "All" is selected
            if (selectedAcceptanceRate === "All" || !selectedAcceptance) {
                filteredBooks2 = filteredBooks; // Show all books if "All" is selected
            } else {
                filteredBooks2 = filteredBooks.filter(book => book.school.acceptance === selectedAcceptance);
            }

            // Display the filtered data
            filteredBooks2.forEach(book => {
                const bookElement = document.createElement('div');
                bookElement.innerHTML = `Name: ${book.school.name}`;
                container.appendChild(bookElement);
            });

            // If no books match the criteria, display a message
            if (filteredBooks2.length === 0) {
                container.innerHTML = 'No schools found for the selected country.';
            }
        })
        .catch(error => console.error('Error:', error));
}




