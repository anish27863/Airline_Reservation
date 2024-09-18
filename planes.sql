CREATE TABLE planes (
    plane_number VARCHAR(7) PRIMARY KEY,
    departure_place VARCHAR(50),
    reaching_place VARCHAR(50),
    departure_time VARCHAR(20),
    arrival_time VARCHAR(20),
    airline_company VARCHAR(50),
    fare1 INT,
    fare2 INT
);
INSERT INTO planes (plane_number, departure_place, reaching_place, departure_time, arrival_time, airline_company, fare1, fare2)
VALUES
    ('AI120', 'Kolkata', 'Chennai', '06:00:00', '08:00:00', 'IndiGo', 9320.0, 9720.0),
    ('VI121', 'Bangalore', 'Hyderabad', '08:00:00', '10:00:00', 'Air India', 9400.0, 9800.0),
    ('SG122', 'Mumbai', 'Delhi', '10:00:00', '12:00:00', 'Vistara', 9480.0, 9980.0),
    ('AI123', 'Chennai', 'Mumbai', '12:00:00', '14:00:00', 'SpiceJet', 9560.0, 10060.0),
    ('VI124', 'Hyderabad', 'Kolkata', '14:00:00', '16:00:00', 'GoAir', 9640.0, 10140.0),
    ('SG125', 'Delhi', 'Bangalore', '16:00:00', '18:00:00', 'IndiGo', 9720.0, 10220.0),
    ('AI126', 'Bangalore', 'Mumbai', '18:00:00', '20:00:00', 'Air India', 9800.0, 10300.0),
    ('VI127', 'Mumbai', 'Delhi', '20:00:00', '22:00:00', 'Vistara', 9880.0, 10380.0),
    ('SG128', 'Chennai', 'Kolkata', '22:00:00', '00:00:00', 'SpiceJet', 9960.0, 10460.0),
    ('AI129', 'Hyderabad', 'Bangalore', '00:00:00', '02:00:00', 'GoAir', 10040.0, 10540.0),
    ('VI130', 'Kolkata', 'Chennai', '02:00:00', '04:00:00', 'IndiGo', 10120.0, 10620.0),
    ('SG131', 'Bangalore', 'Hyderabad', '04:00:00', '06:00:00', 'Air India', 10200.0, 10700.0),
    ('AI132', 'Mumbai', 'Delhi', '06:00:00', '08:00:00', 'Vistara', 10280.0, 10780.0),
    ('VI133', 'Chennai', 'Mumbai', '08:00:00', '10:00:00', 'SpiceJet', 10360.0, 10860.0),
    ('SG134', 'Hyderabad', 'Kolkata', '10:00:00', '12:00:00', 'GoAir', 10440.0, 10940.0),
    ('AI135', 'Kolkata', 'Chennai', '12:00:00', '14:00:00', 'IndiGo', 10520.0, 11020.0),
    ('VI136', 'Bangalore', 'Hyderabad', '14:00:00', '16:00:00', 'Air India', 10600.0, 11100.0),
    ('SG137', 'Mumbai', 'Delhi', '16:00:00', '18:00:00', 'Vistara', 10680.0, 11180.0),
    ('AI138', 'Chennai', 'Mumbai', '18:00:00', '20:00:00', 'SpiceJet', 10760.0, 11260.0),
    ('VI139', 'Hyderabad', 'Kolkata', '20:00:00', '22:00:00', 'GoAir', 10840.0, 11340.0),
    ('SG140', 'Delhi', 'Bangalore', '22:00:00', '00:00:00', 'IndiGo', 10920.0, 11420.0);

    UPDATE planes
    SET fare2 = 2 * fare1;