import csv
import mysql.connector


mydb = mysql.connector.connect(
  host="172.17.0.2",
  user="username",
  password="password",
  database="gestionale"
)


#put_record(table='test', data={'a': 'pippo', 'b': 'pluto'})

with open('calls.csv', 'rt') as in_csv:
    operators = []
    clients = []
    reader = csv.DictReader(in_csv)
    for row in reader:
        operators.append(row['caller_number'])
        clients.append(row['recipient_number'])
    print(operators)
    operators = list(set(operators))
    clients = list(set(clients))


    operators_names = [
        'Emily Johnson', 'Michael Brown', 'Olivia Williams', 'James Davis', 'Isabella Garcia', 'Ethan Martinez',
        'Sophia Anderson', 'Daniel Rodriguez', 'Mia Thomas', 'William Moore'
    ]
    companies_names = [
        "TechNova Solutions", "Quantum Industries", "GreenLeaf Corporation", "BlueWave Technologies",
        "Pinnacle Innovations", "Apex Dynamics", "Fusion Enterprises", "Skyline Ventures", "Nimbus Networks",
        "Solaris Systems", "Vanguard Tech", "Atlas Global", "SynergyWorks", "Echo Technologies", "Summit Enterprises",
        "CrystalTech", "Zenith Innovations", "Nimbus Labs", "Vertex Global", "Orion Systems", "BlueSky Industries",
        "Horizon Solutions", "Optima Ventures", "Pulse Technologies", "Streamline Dynamics", "Elevate Enterprises",
        "Titan Solutions", "NovaTech", "Prime Innovations", "Infinity Labs", "Spectrum Global", "OmniTech Systems",
        "NextGen Solutions", "Stellar Technologies", "Vortex Enterprises", "Paragon Systems", "Ignite Industries",
        "Innovative Ventures", "Radiant Tech", "Axiom Global", "Echo Dynamics", "Catalyst Innovations",
        "Falcon Systems",
        "WaveTech", "Lumina Industries", "Edge Solutions", "Elemental Labs", "Aspire Technologies", "Nexis Ventures",
        "Zenith Dynamics", "Summit Systems", "EvoTech Solutions", "Vector Innovations", "Sierra Tech", "Phoenix Global",
        "CoreTech Systems", "Lunar Dynamics", "Voyage Enterprises", "Veridian Solutions", "Helix Technologies",
        "BrightMind Ventures", "NovaCore Industries", "Pulse Labs", "EcoDynamics", "SparkTech", "Vertex Solutions",
        "BlueStone Technologies", "Elevate Global", "Fusion Systems", "Clarity Innovations", "Pioneer Labs",
        "Axis Global", "SonicTech", "Trident Enterprises", "Beacon Technologies", "Vertex Ventures", "Arctic Systems",
        "PrimeCore Solutions", "Nexis Labs", "QuantumTech", "Apollo Innovations", "Terra Solutions", "Skyline Dynamics",
        "Infinity Systems", "Optimum Ventures", "LunarTech", "Stellar Labs", "Titan Ventures", "Synergy Systems",
        "Horizon Innovations", "Arcadia Global", "AscendTech", "Cobalt Enterprises", "Radiance Technologies",
        "Vanguard Dynamics", "EchoCore Solutions", "Omega Innovations", "Nimbus Technologies", "Quantum Labs",
        "OrionTech"
    ]
    print(len(companies_names))
    operators_dict = {}
    for i, operator in enumerate(operators_names):
        operators_dict[operator] = operators[i]

    companies_dict = {}
    for i, client in enumerate(companies_names):
        companies_dict[client] = clients[i]
    cursor = mydb.cursor()
    for key, value in operators_dict.items():
        cursor.execute(f"INSERT INTO operatori (nome, numero_telefono) VALUES ('{key}', '{value}')")

    for key, value in companies_dict.items():
        cursor.execute(f"INSERT INTO clienti (nome_azienda, numero_azienda) VALUES ('{key}', '{value}')")
    mydb.commit()
    cursor.close()

    print(operators_dict)
    print(companies_dict)