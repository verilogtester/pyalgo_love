# Auto generation of Functional Safety Fault Simulation Testbench
====================================================================

Takes the Functional Safety inputs like Observation and Detection point. It includes information about CLOCK, RESET, Conditional Injection of faults, and time dependency for fault injection etc. 

This python code parse the testbench template and update the user defined strobe points.
#Python features are used to extract the strobe location.
-- created a dictionary of regular expressions used to extract the strobe locations
-- traversing regular expressions in a dictionary 
-- parsing command line options for ease of use
-- replacing global/generic values with the new user provided values like clock, reset, time to inject faults etc. 
-- created a class of multiple function definitions 
-- generating multiple test benches per test vector. 

This code is modular and manageable, idea is to change the regular expressions at a location for the variable inputs for a IP/SoC. 
