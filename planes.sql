use airline

CREATE TABLE planes (
    plane_Number VARCHAR(50),
    departure_place VARCHAR(50),
    reaching_place VARCHAR(50),
    departure_time VARCHAR(8),
    arrival_time VARCHAR(8),
    airline_company varchar(20)
);

INSERT INTO planes (plane_Number, departure_place, reaching_place, departure_time, arrival_time, airline_company)
VALUES
    ('AK123', 'Mumbai', 'Delhi', '09:00:00', '11:00:00', 'AirAsia India'),
    ('UK456', 'Chennai', 'Kolkata', '13:00:00', '15:00:00', 'GoFirst'),
    ('JK789', 'Hyderabad', 'Bangalore', '17:00:00', '19:00:00', 'Air India'),
    ('LK012', 'Ahmedabad', 'Pune','20:00:00', '22:00:00', 'SpiceJet'),
    ('MK345', 'Lucknow', 'Jaipur', '07:00:00', '09:00:00', 'IndiGo'),
    ('BK123', 'Delhi', 'Mumbai', '10:00:00', '12:00:00', 'Vistara'),
    ('CK456', 'Kolkata', 'Chennai','14:00:00', '16:00:00', 'AirAsia India'),
    ('DK789', 'Bangalore', 'Hyderabad', '18:00:00', '20:00:00', 'GoFirst'),
    ('EK012', 'Pune', 'Ahmedabad','21:00:00', '23:00:00', 'Air India'),
    ('FK345', 'Lucknow', 'Jaipur','08:00:00', '10:00:00', 'SpiceJet'),
    ('GL123', 'Mumbai', 'Delhi', '11:00:00', '13:00:00', 'IndiGo'),
    ('HM456', 'Chennai', 'Kolkata','15:00:00', '17:00:00', 'Vistara'),
    ('IN789', 'Hyderabad', 'Bangalore', '19:00:00', '21:00:00', 'AirAsia India'),
    ('JO012', 'Ahmedabad', 'Pune', '22:00:00', '00:00:00', 'GoFirst'),
    ('KP345', 'Lucknow', 'Jaipur','06:00:00', '08:00:00', 'Air India'),
    ('QL123', 'Mumbai', 'Delhi','12:00:00', '14:00:00', 'SpiceJet'),
    ('RM456', 'Chennai', 'Kolkata','16:00:00', '18:00:00', 'IndiGo'),
    ('SN789', 'Hyderabad', 'Bangalore','20:00:00', '22:00:00', 'Vistara'),
    ('TO012', 'Ahmedabad', 'Pune','00:00:00', '02:00:00', 'AirAsia India'),
    ('UP345', 'Lucknow', 'Jaipur','04:00:00', '06:00:00', 'GoFirst'),
    ('VL123', 'Mumbai', 'Delhi','13:00:00', '15:00:00', 'Air India'),
    ('WM456', 'Chennai', 'Kolkata','17:00:00', '19:00:00', 'SpiceJet'),
    ('XN789', 'Hyderabad', 'Bangalore','21:00:00', '23:00:00', 'IndiGo'),
    ('YO012', 'Ahmedabad', 'Pune','01:00:00', '03:00:00', 'Vistara'),
    ('ZP345', 'Lucknow', 'Jaipur','05:00:00', '07:00:00', 'AirAsia India'); 