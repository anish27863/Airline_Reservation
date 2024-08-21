use airline

CREATE TABLE planes (
    airline_name VARCHAR(50),
    departure_place VARCHAR(50),
    reaching_place VARCHAR(50),
    plane_number VARCHAR(20),
    departure_time TIME,
    arrival_time TIME,
    airline_company varchar(20)
);

INSERT INTO planes (airline_name, departure_place, reaching_place, plane_number, departure_time, arrival_time, airline_company)
VALUES
    ('AK123', 'Mumbai', 'Delhi', 'AK123', '09:00:00', '11:00:00', 'AirAsia India'),
    ('UK456', 'Chennai', 'Kolkata', 'UK456', '13:00:00', '15:00:00', 'GoFirst'),
    ('JK789', 'Hyderabad', 'Bangalore', 'JK789', '17:00:00', '19:00:00', 'Air India'),
    ('LK012', 'Ahmedabad', 'Pune', 'LK012', '20:00:00', '22:00:00', 'SpiceJet'),
    ('MK345', 'Lucknow', 'Jaipur', 'MK345', '07:00:00', '09:00:00', 'IndiGo'),
    ('BK123', 'Delhi', 'Mumbai', 'BK123', '10:00:00', '12:00:00', 'Vistara'),
    ('CK456', 'Kolkata', 'Chennai', 'CK456', '14:00:00', '16:00:00', 'AirAsia India'),
    ('DK789', 'Bangalore', 'Hyderabad', 'DK789', '18:00:00', '20:00:00', 'GoFirst'),
    ('EK012', 'Pune', 'Ahmedabad', 'EK012', '21:00:00', '23:00:00', 'Air India'),
    ('FK345', 'Lucknow', 'Jaipur', 'FK345', '08:00:00', '10:00:00', 'SpiceJet'),
    ('GL123', 'Mumbai', 'Delhi', 'GL123', '11:00:00', '13:00:00', 'IndiGo'),
    ('HM456', 'Chennai', 'Kolkata', 'HM456', '15:00:00', '17:00:00', 'Vistara'),
    ('IN789', 'Hyderabad', 'Bangalore', 'IN789', '19:00:00', '21:00:00', 'AirAsia India'),
    ('JO012', 'Ahmedabad', 'Pune', 'JO012', '22:00:00', '00:00:00', 'GoFirst'),
    ('KP345', 'Lucknow', 'Jaipur', 'KP345', '06:00:00', '08:00:00', 'Air India'),
    ('QL123', 'Mumbai', 'Delhi', 'QL123', '12:00:00', '14:00:00', 'SpiceJet'),
    ('RM456', 'Chennai', 'Kolkata', 'RM456', '16:00:00', '18:00:00', 'IndiGo'),
    ('SN789', 'Hyderabad', 'Bangalore', 'SN789', '20:00:00', '22:00:00', 'Vistara'),
    ('TO012', 'Ahmedabad', 'Pune', 'TO012', '00:00:00', '02:00:00', 'AirAsia India'),
    ('UP345', 'Lucknow', 'Jaipur', 'UP345', '04:00:00', '06:00:00', 'GoFirst'),
    ('VL123', 'Mumbai', 'Delhi', 'VL123', '13:00:00', '15:00:00', 'Air India'),
    ('WM456', 'Chennai', 'Kolkata', 'WM456', '17:00:00', '19:00:00', 'SpiceJet'),
    ('XN789', 'Hyderabad', 'Bangalore', 'XN789', '21:00:00', '23:00:00', 'IndiGo'),
    ('YO012', 'Ahmedabad', 'Pune', 'YO012', '01:00:00', '03:00:00', 'Vistara'),
    ('ZP345', 'Lucknow', 'Jaipur', 'ZP345', '05:00:00', '07:00:00', 'AirAsia India');