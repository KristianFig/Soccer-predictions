document.addEventListener('DOMContentLoaded', function() {
  const team1Select = document.getElementById('team1');
  const team2Select = document.getElementById('team2');
  const predictButton = document.getElementById('predictButton');
  const resultDiv = document.getElementById('result');

  // Function to fetch team names and populate dropdowns
  function fetchTeamNames() {
      fetch('http://127.0.0.1:5000/get_team_names')
          .then(response => response.json())
          .then(data => {
              data.teams.forEach(team => {
                  const option1 = document.createElement('option');
                  option1.text = team;
                  team1Select.add(option1);

                  const option2 = document.createElement('option');
                  option2.text = team;
                  team2Select.add(option2);
              });
          })
          .catch(error => console.error('Error fetching teams:', error));
  }

  // Function to predict the winner
  function predictWinner(team1, team2) {
      fetch(`http://127.0.0.1:5000/predict_winner?team_1=${team1}&team_2=${team2}`)
          .then(response => response.json())
          .then(data => {
              resultDiv.textContent = `Winner: ${data.winner_of_match}`;
          })
          .catch(error => console.error('Error predicting winner:', error));
  }

  // Event listener for predict button click
  predictButton.addEventListener('click', function() {
      const selectedTeam1 = team1Select.value;
      const selectedTeam2 = team2Select.value;

      if (selectedTeam1 && selectedTeam2) {
          predictWinner(selectedTeam1, selectedTeam2);
      } else {
          resultDiv.textContent = 'Please select both teams.';
      }
  });

  // Fetch team names when the page loads
  fetchTeamNames();
});