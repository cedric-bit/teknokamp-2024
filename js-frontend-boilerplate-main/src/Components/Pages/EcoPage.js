import Chart from 'chart.js/auto';

const createChart = (context, config) => new Chart(context, config);

const EcoPage = () => {
    const main = document.querySelector('main');
    main.innerHTML = `
        <h3>Welcome to your Eco-Responsability page!</h3>
        <div class="chart-container">
            <canvas id="energyChart"></canvas>
            <canvas id="priceChart"></canvas>
            <canvas id="impactChart"></canvas>
        </div>
    `;
    const energyCtx = document.getElementById('energyChart').getContext('2d');

    
    const priceCtx = document.getElementById('priceChart').getContext('2d');
    const impactCtx = document.getElementById('impactChart').getContext('2d');

    const energyData = [25, 25, 20, 15, 15];
    const priceData = [40, 60, 50, 30, 20];
    const impactData = [40, 60];

  
    
    const energyChart = createChart(energyCtx, {
        type: 'pie',
        data: {
            labels: ['Soleil', 'éoliennes', 'thermique', 'nucléaire', 'hydrogène'],
            datasets: [{ data: energyData, backgroundColor: ['red', 'blue', 'yellow', 'green', 'purple'] }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: 'Consommation d\'énergie'
                }
            }
        },
    });

    const priceChart = createChart(priceCtx, {
        type: 'pie',
        data: {
            labels: ['PRIX SOL', 'PRIX EOL', 'PRIX THER', 'PRIX NUC', 'PRIX HYD'],
            datasets: [{ data: priceData, backgroundColor: ['red', 'blue', 'yellow', 'green', 'purple'] }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'left',
                },
                title: {
                    display: true,
                    text: 'Prix de l\'énergie'
                }
            }
        },
    });

    createChart(impactCtx, {
        type: 'pie',
        data: {
            labels: ['HYDR VERT', 'THERMAL'],
            datasets: [{ data: impactData, backgroundColor: ['green', 'orange'] }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'bottom',
                },
                title: {
                    display: true,
                    text: 'Impact Énergétique'
                }
            }
        },
    });

    energyChart.canvas.addEventListener('click', (event) => {
        const activePoints = energyChart.getElementsAtEventForMode(event, 'nearest', { intersect: true }, true);
        if (activePoints.length) {
            const { index } = activePoints[0];
            energyData[index] += 1;  // Augmente la consommation
            energyChart.update();

            // Logique pour augmenter le prix
            if (index < priceData.length) {
                priceData[index] += index + 1;  // Exemple: augmenter plus pour les premiers éléments
                priceChart.update();
            }
        }
    });

    priceChart.canvas.addEventListener('click', (event) => {
        const activePoints = priceChart.getElementsAtEventForMode(event, 'nearest', { intersect: true }, true);
        if (activePoints.length) {
            const { index } = activePoints[0];
            
            priceData[index] += 5;  // Ajoute une quantité significative pour voir le changement
            priceChart.update();
    
            // Si vous voulez lier cela avec les autres graphiques, ajoutez la logique correspondante ici
            // Par exemple, augmenter l'impact ou la consommation d'énergie en fonction du prix cliqué
            impactData[index] += 10; // exemple de modification des données d'impact
            energyChart.update();
        }
    });
    

    
};

export default EcoPage;