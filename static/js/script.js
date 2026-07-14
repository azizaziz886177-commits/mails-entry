// ================================
// MailSentry Insight - script.js
// ================================

console.log("MailSentry Insight Loaded Successfully");

// Search emails in dashboard table
function searchEmails() {
    let input = document.getElementById("searchInput");
    let filter = input.value.toUpperCase();

    let table = document.getElementById("emailTable");

    if (!table) return;

    let tr = table.getElementsByTagName("tr");

    for (let i = 1; i < tr.length; i++) {

        let showRow = false;

        let td = tr[i].getElementsByTagName("td");

        for (let j = 0; j < td.length; j++) {

            if (td[j]) {

                let txtValue = td[j].textContent || td[j].innerText;

                if (txtValue.toUpperCase().indexOf(filter) > -1) {
                    showRow = true;
                    break;
                }
            }
        }

        tr[i].style.display = showRow ? "" : "none";
    }
}

// Confirm before refreshing emails
function refreshEmails() {

    if (confirm("Fetch latest emails from Gmail?")) {
        window.location.href = "/refresh";
    }
}

// Auto-refresh every 5 minutes
setInterval(function () {
    console.log("Checking for updates...");
}, 300000);

// Highlight selected row
document.addEventListener("DOMContentLoaded", function () {

    let table = document.getElementById("emailTable");

    if (!table) return;

    let rows = table.getElementsByTagName("tr");

    for (let i = 1; i < rows.length; i++) {

        rows[i].addEventListener("click", function () {

            for (let j = 1; j < rows.length; j++) {
                rows[j].style.backgroundColor = "";
            }

            this.style.backgroundColor = "#d6eaf8";
        });
    }
});