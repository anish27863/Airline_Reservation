use airline

CREATE TABLE planes (
    airline_name VARCHAR(50),
    departure_place VARCHAR(50),
    reaching_place VARCHAR(50),
    plane_number VARCHAR(20),
    departure_time TIME,
    arrival_time TIME
);

INSERT INTO planes (airline_name, departure_place, reaching_place, plane_number, departure_time, arrival_time)
VALUES
    ('VL123', 'Mumbai', 'Delhi', 'VL123', '13:00:00', '15:00:00'),
    ('WM456', 'Chennai', 'Kolkata', 'WM456', '17:00:00', '19:00:00'),
    ('XN789', 'Hyderabad', 'Bangalore', 'XN789', '21:00:00', '23:00:00'),
    ('YO012', 'Ahmedabad', 'Pune', 'YO012', '01:00:00', '03:00:00'),
    ('ZP345', 'Lucknow', 'Jaipur', 'ZP345', '05:00:00', '07:00:00'),
    ('AR123', 'Mumbai', 'Delhi', 'AR123', '14:00:00', '16:00:00'),
    ('BS456', 'Chennai', 'Kolkata', 'BS456', '18:00:00', '20:00:00'),
    ('CT789', 'Hyderabad', 'Bangalore', 'CT789', '22:00:00', '00:00:00'),
    ('DU012', 'Ahmedabad', 'Pune', 'DU012', '02:00:00', '04:00:00'),
    ('EV345', 'Lucknow', 'Jaipur', 'EV345', '06:00:00', '08:00:00'),
    ('FW123', 'Mumbai', 'Delhi', 'FW123', '15:00:00', '17:00:00'),
    ('GX456', 'Chennai', 'Kolkata', 'GX456', '19:00:00', '21:00:00'),
    ('HY789', 'Hyderabad', 'Bangalore', 'HY789', '23:00:00', '01:00:00'),
    ('IZ012', 'Ahmedabad', 'Pune', 'IZ012', '03:00:00', '05:00:00'),
    ('JK345', 'Lucknow', 'Jaipur', 'JK345', '07:00:00', '09:00:00'),
    ('KL123', 'Mumbai', 'Delhi', 'KL123', '16:00:00', '18:00:00'),
    ('LM456', 'Chennai', 'Kolkata', 'LM456', '20:00:00', '22:00:00'),
    ('NO789', 'Hyderabad', 'Bangalore', 'NO789', '00:00:00', '02:00:00'),
    ('PQ012', 'Ahmedabad', 'Pune', 'PQ012', '04:00:00', '06:00:00'),
    ('RS345', 'Lucknow', 'Jaipur', 'RS345', '08:00:00', '10:00:00');