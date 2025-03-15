import streamlit as st
import random
import time
import pandas as pd

# Define the set of questions in the exact format
QUESTIONS = [{"question": "Which type of wind turbine blade design is most commonly used for large-scale wind farms?\nA) Horizontal-axis\nB) Vertical-axis\nC) Savonius\nD) Darrieus", "answer": "A"},
    {"question": "What is a primary advantage of using a three-blade design over a two-blade design?\nA) Lower cost\nB) Higher stability\nC) Increased noise\nD) Reduced efficiency", "answer": "B"},
    {"question": "What is a common source of energy loss in wind turbine blades?\nA) Blade tip vortices\nB) Generator heat\nC) Transmission lines\nD) Gearbox friction", "answer": "A"},
    {"question": "How can wind turbine blade efficiency be improved?\nA) Adding more blades\nB) Using lighter materials\nC) Reducing blade length\nD) Increasing blade weight", "answer": "B"},
    {"question": "What concept is critical to optimizing blade shape?\nA) Aerodynamics\nB) Thermodynamics\nC) Electromagnetism\nD) Hydrodynamics", "answer": "A"},
    {"question": "Which type of generator is most commonly paired with wind turbines?\nA) Synchronous\nB) Asynchronous\nC) DC generator\nD) Steam turbine", "answer": "B"},
    {"question": "What is a key advantage of doubly-fed induction generators in wind power?\nA) Lower cost\nB) Variable speed operation\nC) Higher weight\nD) Simpler maintenance", "answer": "B"},
    {"question": "What component converts mechanical energy to electrical energy in a wind turbine?\nA) Nacelle\nB) Rotor\nC) Generator\nD) Tower", "answer": "C"},
    {"question": "What is a disadvantage of permanent magnet generators?\nA) High efficiency\nB) High cost of rare-earth materials\nC) Low maintenance\nD) Small size", "answer": "B"},
    {"question": "What factor affects generator efficiency in wind turbines?\nA) Wind speed\nB) Blade color\nC) Tower height\nD) Air temperature", "answer": "A"},
    {"question": "When wind turbines generate excess electricity, which method is commonly used to store it?\nA) Flywheels\nB) Supercapacitors\nC) Compressed air storage\nD) Batteries", "answer": "D"},
    {"question": "How can energy storage systems enhance wind power integration into the grid?\nA) Increasing turbine efficiency\nB) Stabilizing grid frequency\nC) Reducing backup plants\nD) Supplying endless power", "answer": "B"},
    {"question": "What is the main challenge of power storage for wind turbines?\nA) High initial cost\nB) Difficulty converting energy\nC) Limited storage space\nD) Slow discharge", "answer": "A"},
    {"question": "What happens during the discharge of a battery storage system?\nA) Chemical energy converts to electrical\nB) Electrical energy converts to heat\nC) Wind speed increases\nD) Grid shuts down", "answer": "A"},
    {"question": "Which storage method has the fastest response time?\nA) Pumped hydro\nB) Batteries\nC) Flywheels\nD) Thermal storage", "answer": "C"},
    {"question": "What is the primary method for transmitting electricity from wind farms?\nA) Underground cables\nB) Overhead lines\nC) Wireless transmission\nD) Pipelines", "answer": "B"},
    {"question": "How is power commonly lost in transmission lines?\nA) Radiation\nB) Resistance heating\nC) Wind interference\nD) Blade friction", "answer": "B"},
    {"question": "What can reduce power loss in transmission?\nA) Higher voltage\nB) Thicker cables\nC) Shorter distances\nD) All of the above", "answer": "D"},
    {"question": "What device steps up voltage for long-distance transmission?\nA) Transformer\nB) Generator\nC) Inverter\nD) Capacitor", "answer": "A"},
    {"question": "Why is AC preferred over DC for long-distance power transmission?\nA) Lower cost\nB) Easier voltage transformation\nC) Higher efficiency\nD) Less maintenance", "answer": "B"},
    {"question": "What is a key factor in siting a wind farm?\nA) Proximity to cities\nB) Consistent wind speed\nC) Flat terrain\nD) Low cost land", "answer": "B"},
    {"question": "What is a challenge in installing offshore wind turbines?\nA) High wind speeds\nB) Foundation stability\nC) Low maintenance\nD) Easy access", "answer": "B"},
    {"question": "What permit is typically required for wind farm installation?\nA) Environmental impact assessment\nB) Building permit\nC) Noise permit\nD) Water usage permit", "answer": "A"},
    {"question": "When was the first windmill used for electricity generation?\nA) 1887\nB) 1900\nC) 1925\nD) 1950", "answer": "A"},
    {"question": "What is a modern environmental benefit of wind power?\nA) Increased noise\nB) Reduced carbon emissions\nC) Higher water use\nD) Land degradation", "answer": "B"},
    {"question": "What is an essential factor in designing efficient wind turbine blades?\nA) Material color\nB) Blade shape and aerodynamics\nC) Number of blades\nD) Height of the turbine", "answer": "B"},
    {"question": "How does increasing the number of blades on a wind turbine generally affect its performance?\nA) It decreases efficiency\nB) No effect on performance\nC) It helps generate electricity at lower wind speeds\nD) It increases the turbine's rotational speed", "answer": "C"},
    {"question": "Which material is most commonly used in modern wind turbine blades due to its strength-to-weight ratio?\nA) Steel\nB) Aluminum\nC) Carbon fiber\nD) Fiberglass", "answer": "D"},
    {"question": "What is a major benefit of using direct-drive generators in wind turbines?\nA) Reduced noise levels\nB) Simplified mechanical design\nC) Increased speed of rotation\nD) More complex maintenance", "answer": "B"},
    {"question": "How do power generators in wind turbines convert energy?\nA) Convert electrical energy to mechanical energy\nB) Convert wind energy to thermal energy\nC) Convert mechanical energy to electrical energy\nD) Convert thermal energy to sound energy", "answer": "C"},
    {"question": "Which component of a wind turbine generator is responsible for controlling voltage and frequency?\nA) Gearbox\nB) Rotor hub\nC) Converter\nD) Breaker switch", "answer": "C"},
    {"question": "What is a key challenge in storing wind-generated power?\nA) Low battery cost\nB) Predictable power supply\nC) Variable power output with changing winds\nD) Lack of suitable storage technology", "answer": "C"},
    {"question": "What storage technology is commonly paired with wind power to balance energy supply and demand?\nA) Traditional fuel cells\nB) Lithium-ion batteries\nC) Hydraulic pump storage\nD) Coal reserves", "answer": "B"},
    {"question": "Which is a future prospect for utility-scale storage of wind power?\nA) Fossil fuels\nB) Graphene supercapacitors\nC) Natural gas storage\nD) Wood pellets", "answer": "B"},
    {"question": "What is the main purpose of power transmission lines in wind energy systems?\nA) To increase the voltage of generated electricity\nB) To distribute electricity to storage points\nC) To transfer generated electricity from turbines to the grid\nD) To transform electricity into hydrogen", "answer": "C"},
    {"question": "How can transmission losses be minimized in wind power systems?\nA) Using copper instead of aluminum transmission lines\nB) Increasing the resistance in power lines\nC) Reducing the voltage in power lines\nD) Increasing the voltage in power lines", "answer": "D"},
    {"question": "Which factor must be considered when planning the siting of wind farms?\nA) Proximity to major cities\nB) Historical site value\nC) Wind resource assessment\nD) Stock market trends", "answer": "C"},
    {"question": "What is essential to assess before installing a wind turbine?\nA) Soil type at the site\nB) Temperature range of the location\nC) Presence of bird migration routes\nD) Wind speed and direction statistics", "answer": "D"},
    {"question": "Which regulatory consideration is critical in the wind energy siting process?\nA) Trade tariffs\nB) Zoning laws and permits\nC) Internet connectivity\nD) Labor union presence", "answer": "B"},
    {"question": "What historical milestone marked the widespread use of wind power for electricity generation?\nA) Invention of the steam engine\nB) Development of grid-tied wind systems\nC) Invention of the internal combustion engine\nD) Discovery of electricity", "answer": "B"},
    {"question": "When and where was the first electricity-generating wind turbine built?\nA) 1888 in Cleveland, Ohio\nB) 1903 in Detroit, Michigan\nC) 1950 in Copenhagen, Denmark\nD) 1927 in Amarillo, Texas", "answer": "A"},
    {"question": "Which nation currently leads in worldwide operational wind power capacity?\nA) Germany\nB) United States\nC) China\nD) Denmark", "answer": "C"},
    {"question": "What was a major factor in the 1970s that spurred interest and investment in wind power?\nA) Increase in coal power\nB) Rise of the environmental movement\nC) Oil crisis\nD) Advances in solar technology", "answer": "C"},
    {"question": "What significant development in wind power occurred in the 1990s?\nA) Introduction of offshore wind farms\nB) Discovery of wind energy\nC) Decline in fossil fuel usage\nD) Invention of horizontal-axis turbines", "answer": "A"},
    {"question": "How can optimizing the location of wind turbines reduce costs?\nA) By increasing maintenance needs\nB) By shortening transmission distances\nC) By decreasing wind speed variance\nD) By needing fewer access roads", "answer": "B"},
    {"question": "What technology is used to ensure wind turbines generate optimal energy despite changing wind directions?\nA) Propeller orientation\nB) Fixed platform design\nC) Active yaw control systems\nD) Magnetic levitation", "answer": "C"},
    {"question": "Which consideration is crucial for selecting the height of a wind turbine tower?\nA) Surface roughness and turbulence intensity\nB) Distance to the nearest city\nC) Length of turbine blades\nD) Proximity to highways", "answer": "A"},
    {"question": "How does offshore wind power benefit from location?\nA) Greater biodiversity impact\nB) Less impact from city pollution\nC) Higher and more consistent wind speeds\nD) Easier transmission to the grid", "answer": "C"},
    {"question": "What is a common method used to secure a wind turbine tower to the ground?\nA) Sandbag barriers\nB) Guy wires and anchors\nC) Concrete foundations\nD) Direct earth embedment", "answer": "C"},
    {"question": "Which of these acts as a maintenance and safety feature in a wind turbine?\nA) Power amplifier\nB) Beverage cooler\nC) Emergency brake system\nD) Vibration enhancer", "answer": "C"},
    {"question": "What is the primary function of a wind turbine's pitch control system?\nA) Adjust blade angle\nB) Control yaw\nC) Monitor wind speed\nD) Regulate generator output", "answer": "A"},
    {"question": "Which material is increasingly used for modern wind turbine blades due to its high strength-to-weight ratio?\nA) Steel\nB) Aluminum\nC) Carbon fiber composites\nD) Wood", "answer": "C"},
    {"question": "What is the purpose of blade twist in wind turbine design?\nA) Increase noise\nB) Maintain optimal angle of attack\nC) Reduce blade length\nD) Enhance visual appeal", "answer": "B"},
    {"question": "What is the Betz limit?\nA) Maximum wind speed\nB) Maximum theoretical efficiency of a wind turbine\nC) Minimum blade length\nD) Maximum generator output", "answer": "B"},
    {"question": "What is the main advantage of using airfoil-shaped blades?\nA) Reduced cost\nB) Increased lift and reduced drag\nC) Simplified manufacturing\nD) Enhanced visual impact", "answer": "B"},
    {"question": "What is the role of the converter in a variable-speed wind turbine?\nA) Increase turbine height\nB) Convert variable frequency AC to grid frequency AC\nC) Cool the generator\nD) Control blade pitch", "answer": "B"},
    {"question": "What is the advantage of using a direct-drive generator?\nA) Lower cost\nB) Elimination of gearbox\nC) Increased noise\nD) Reduced efficiency", "answer": "B"},
    {"question": "What is the primary function of the slip rings in a wound rotor induction generator?\nA) Cool the generator\nB) Connect the rotor to external resistors\nC) Control blade pitch\nD) Monitor wind speed", "answer": "B"},
    {"question": "What is the impact of generator pole number on its rotational speed?\nA) Higher pole number, higher speed\nB) Lower pole number, higher speed\nC) Pole number does not affect speed\nD) Speed is only affected by wind speed", "answer": "B"},
    {"question": "What is a key benefit of using a synchronous generator with a full converter?\nA) Reduced weight\nB) Decoupling of the generator from the grid frequency\nC) Lower cost\nD) Simplified maintenance", "answer": "B"},
    {"question": "What is the primary application of pumped hydro storage in wind energy systems?\nA) Short-term frequency regulation\nB) Long-duration energy storage\nC) Direct turbine cooling\nD) Blade cleaning", "answer": "B"},
    {"question": "What is the role of a battery management system (BMS) in a wind turbine storage setup?\nA) Control wind speed\nB) Monitor and control battery charging and discharging\nC) Adjust blade pitch\nD) Regulate generator output", "answer": "B"},
    {"question": "What is a significant advantage of using flow batteries for wind energy storage?\nA) High energy density\nB) Scalability and long cycle life\nC) Low initial cost\nD) Small size", "answer": "B"},
    {"question": "What is the principle behind using thermal energy storage in wind power systems?\nA) Converting heat to electricity directly\nB) Storing excess electricity as heat\nC) Cooling turbine components\nD) Heating wind turbines", "answer": "B"},
    {"question": "What is the purpose of a supercapacitor in a wind turbine's energy storage system?\nA) Long-term storage\nB) Providing short bursts of power for grid stabilization\nC) Cooling the generator\nD) Adjusting blade angle", "answer": "B"},
    {"question": "What is the purpose of a substation in a wind farm's transmission system?\nA) Increase wind speed\nB) Step up voltage and connect to the grid\nC) Store energy\nD) Control blade pitch", "answer": "B"},
    {"question": "What is the advantage of using High Voltage Direct Current (HVDC) transmission for offshore wind farms?\nA) Lower cost\nB) Reduced losses over long distances\nC) Simpler maintenance\nD) Increased wind speed", "answer": "B"},
    {"question": "What is the role of a smart grid in integrating wind power?\nA) Increase wind speed\nB) Manage and optimize power flow from variable renewable sources\nC) Control blade pitch\nD) Store energy", "answer": "B"},
    {"question": "What is the function of a phase-locked loop (PLL) in grid-connected wind turbines?\nA) Increase wind speed\nB) Synchronize the turbine's output with the grid frequency\nC) Control blade pitch\nD) Store energy", "answer": "B"},
    {"question": "What is the purpose of reactive power compensation in wind farm transmission?\nA) Increase wind speed\nB) Maintain grid voltage stability\nC) Control blade pitch\nD) Store energy", "answer": "B"},
    {"question": "What is a key consideration for minimizing environmental impact during wind farm construction?\nA) Increasing noise levels\nB) Protecting local wildlife and habitats\nC) Reducing land use\nD) Increasing turbine height", "answer": "B"},
    {"question": "What is a LiDAR system used for in wind farm site assessment?\nA) Measuring wind speed and direction\nB) Controlling blade pitch\nC) Storing energy\nD) Cooling the generator", "answer": "A"},
    {"question": "What is a key factor in determining the spacing between wind turbines in a wind farm?\nA) Turbine color\nB) Minimizing wake effects\nC) Increasing noise levels\nD) Reducing land use", "answer": "B"},
    {"question": "What was a primary use of early windmills before electricity generation?\nA) Transportation\nB) Grinding grain and pumping water\nC) Communication\nD) Heating", "answer": "B"},
    {"question": "What is a modern application of small-scale wind turbines?\nA) Large-scale grid power\nB) Off-grid power for remote locations\nC) Cooling power plants\nD) Heating large buildings", "answer": "B"},
    {"question": "What design feature helps mitigate blade icing in cold climates?\nA) Increased blade thickness\nB) Heating elements within the blade\nC) Reduced blade length\nD) Increased blade curvature", "answer": "B"},
    {"question": "What is the primary effect of increasing the solidity of a wind turbine rotor?\nA) Increased speed\nB) Increased torque\nC) Reduced efficiency\nD) Reduced noise", "answer": "B"},
    {"question": "What is the function of the blade root in a wind turbine?\nA) Generate lift\nB) Connect the blade to the hub\nC) Control pitch\nD) Reduce drag", "answer": "B"},
    {"question": "What is the concept of 'stall regulation' in wind turbine control?\nA) Adjusting generator speed\nB) Using blade pitch to limit power\nC) Allowing blades to stall at high wind speeds\nD) Controlling yaw", "answer": "C"},
    {"question": "What is the impact of blade surface roughness on aerodynamic performance?\nA) Increases lift\nB) Increases drag\nC) No significant impact\nD) Reduces noise", "answer": "B"},
    {"question": "What is the primary advantage of using a wound rotor induction generator (WRIG) in variable-speed wind turbines?\nA) Lower cost\nB) Ability to control rotor current\nC) Higher efficiency at all speeds\nD) Reduced weight", "answer": "B"},
    {"question": "What is the role of the gearbox in a traditional wind turbine drivetrain?\nA) Generate electricity\nB) Increase rotational speed for the generator\nC) Control blade pitch\nD) Cool the generator", "answer": "B"},
    {"question": "What is the impact of temperature on the performance of a permanent magnet generator?\nA) Increased efficiency\nB) Decreased efficiency and potential demagnetization\nC) No impact\nD) Increased speed", "answer": "B"},
    {"question": "What is the function of the excitation system in a synchronous generator?\nA) Control blade pitch\nB) Provide DC current to the rotor\nC) Cool the generator\nD) Convert AC to DC", "answer": "B"},
    {"question": "What is the benefit of using a multi-pole generator in a direct-drive wind turbine?\nA) Increased speed\nB) Reduced size and weight\nC) Elimination of gearbox\nD) Increased cost", "answer": "C"},
    {"question": "What is the primary advantage of using vanadium redox flow batteries (VRFBs) for wind energy storage?\nA) High energy density\nB) Long cycle life and independent scaling of power and energy\nC) Low initial cost\nD) Small size", "answer": "B"},
    {"question": "What is the function of an inverter in a battery energy storage system connected to a wind turbine?\nA) Increase wind speed\nB) Convert DC to AC for grid connection\nC) Control blade pitch\nD) Store energy", "answer": "B"},
    {"question": "What is the concept of 'grid-forming' batteries in wind power integration?\nA) Batteries that only store energy\nB) Batteries that can provide voltage and frequency support to the grid\nC) Batteries that control wind turbine speed\nD) Batteries used for blade cleaning", "answer": "B"},
    {"question": "What is the primary limitation of using lithium-ion batteries for large-scale wind energy storage?\nA) Low energy density\nB) Cost and limited cycle life\nC) Slow response time\nD) Large size", "answer": "B"},
    {"question": "What is the role of a power conversion system (PCS) in a wind turbine energy storage system?\nA) Control wind speed\nB) Manage the flow of power between the batteries and the grid\nC) Adjust blade pitch\nD) Cool the generator", "answer": "B"},
    {"question": "What is the purpose of a Static VAR Compensator (SVC) in wind farm grid integration?\nA) Increase wind speed\nB) Provide reactive power support for voltage stability\nC) Control blade pitch\nD) Store energy", "answer": "B"},
    {"question": "What is the advantage of using Flexible AC Transmission Systems (FACTS) devices in wind power transmission?\nA) Lower cost\nB) Enhanced grid stability and power flow control\nC) Simpler maintenance\nD) Increased wind speed", "answer": "B"},
    {"question": "What is the role of a Supervisory Control and Data Acquisition (SCADA) system in wind farm transmission?\nA) Increase wind speed\nB) Monitor and control the transmission network\nC) Control blade pitch\nD) Store energy", "answer": "B"},
    {"question": "What is the function of a fault ride-through (FRT) capability in grid-connected wind turbines?\nA) Increase wind speed\nB) Allow turbines to remain connected during grid disturbances\nC) Control blade pitch\nD) Store energy", "answer": "B"},
    {"question": "What is the purpose of a power quality conditioner in wind farm transmission?\nA) Increase wind speed\nB) Mitigate voltage fluctuations and harmonics\nC) Control blade pitch\nD) Store energy", "answer": "B"},
    {"question": "What is a key consideration for minimizing noise pollution during wind farm operation?\nA) Increasing turbine height\nB) Optimizing turbine spacing and blade design\nC) Reducing land use\nD) Increasing turbine speed", "answer": "B"},
    {"question": "What is a 'wake effect' in wind farms?\nA) Increased wind speed\nB) Reduced wind speed and turbulence behind a turbine\nC) Blade icing\nD) Generator overheating", "answer": "B"},
    {"question": "What is a key factor in selecting foundation type for offshore wind turbines?\nA) Turbine color\nB) Water depth and soil conditions\nC) Noise levels\nD) Land use", "answer": "B"},
    {"question": "What was a significant advancement in wind turbine technology in the late 20th century?\nA) Use of wooden blades\nB) Development of variable-speed turbines\nC) Use of DC generators\nD) Manual pitch control", "answer": "B"},
    {"question": "What is a modern application of floating offshore wind turbines?\nA) Powering remote islands in deep waters\nB) Large scale grid power on land\nC) Cooling power plants\nD) Heating large buildings", "answer": "A"},
    {"question": "What is the primary advantage of using carbon fiber composites in wind turbine blades?\nA) Lower cost\nB) Higher strength-to-weight ratio\nC) Easier manufacturing\nD) Increased flexibility", "answer": "B"},
    {"question": "What aerodynamic phenomenon is mitigated by twisting wind turbine blades along their length?\nA) Tip vortices\nB) Stall at the blade root\nC) Drag divergence\nD) Ground effect", "answer": "B"},
    {"question": "What is the primary purpose of a tapered blade design?\nA) Reduce weight and material costs\nB) Increase noise\nC) Enhance visual appeal\nD) Simplify manufacturing", "answer": "A"},
    {"question": "Which material property is critical for reducing fatigue in wind turbine blades?\nA) High thermal conductivity\nB) High stiffness-to-weight ratio\nC) Electrical conductivity\nD) Magnetic permeability", "answer": "B"},
    {"question": "What role do vortex generators play on wind turbine blades?\nA) Increase drag\nB) Delay flow separation to improve lift\nC) Generate electricity\nD) Reduce icing", "answer": "B"},
    {"question": "What is a key advantage of a doubly-fed induction generator (DFIG)?\nA) Fixed-speed operation\nB) Variable-speed operation with partial-scale converters\nC) No gearbox required\nD) Lower maintenance", "answer": "B"},
    {"question": "Which generator type is most common in direct-drive wind turbines?\nA) Squirrel cage induction\nB) Permanent magnet synchronous\nC) Wound rotor induction\nD) DC generator", "answer": "B"},
    {"question": "What is the function of slip rings in a wound rotor induction generator?\nA) Transfer power to the grid\nB) Allow current to flow to rotor windings\nC) Cool the generator\nD) Control yaw", "answer": "B"},
    {"question": "How do permanent magnet generators differ from induction generators?\nA) Require external DC excitation\nB) Use magnets for field excitation\nC) Lower efficiency\nD) Fixed-speed only", "answer": "B"},
    {"question": "What is a disadvantage of synchronous generators in wind turbines?\nA) Inability to sync with the grid\nB) Brush maintenance\nC) Low torque\nD) High noise", "answer": "B"},
    {"question": "Which technology is best for short-term frequency regulation in wind farms?\nA) Pumped hydro\nB) Flywheels\nC) Lithium-ion batteries\nD) Hydrogen storage", "answer": "B"},
    {"question": "What limits pumped hydro storage for wind energy?\nA) High efficiency\nB) Geographical constraints\nC) Low capacity\nD) Short lifespan", "answer": "B"},
    {"question": "What is the primary use of supercapacitors in wind systems?\nA) Long-term storage\nB) Smoothing rapid power fluctuations\nC) Voltage regulation\nD) Blade heating", "answer": "B"},
    {"question": "Which method stores wind energy as thermal energy?\nA) Batteries\nB) Molten salt systems\nC) Flywheels\nD) Compressed air", "answer": "B"},
    {"question": "What is a challenge for hydrogen storage in wind energy?\nA) Low energy density\nB) High conversion losses\nC) Easy transportation\nD) Abundant infrastructure", "answer": "B"},
    {"question": "Why is HVDC used for offshore wind farms?\nA) Lower cost for short distances\nB) Reduced losses over long distances\nC) Easier installation\nD) Higher AC voltage", "answer": "B"},
    {"question": "What is the role of a step-up transformer in wind farms?\nA) Increase voltage for transmission\nB) Decrease voltage for local use\nC) Convert AC to DC\nD) Store energy", "answer": "A"},
    {"question": "What complicates wind power integration into AC grids?\nA) Intermittency causing frequency fluctuations\nB) Constant output\nC) High inertia\nD) Low voltage", "answer": "A"},
    {"question": "What is 'wind curtailment'?\nA) Reducing wind speed\nB) Reducing output due to grid limits\nC) Increasing efficiency\nD) Storing energy", "answer": "B"},
    {"question": "What is dynamic line rating?\nA) Limiting power flow\nB) Adjusting capacity based on real-time conditions\nC) Increasing voltage\nD) Storing energy", "answer": "B"},
    {"question": "What environmental concern is critical for offshore wind farms?\nA) Air pollution\nB) Marine ecosystem impact\nC) Noise\nD) Visual impact", "answer": "B"},
    {"question": "Why are turbines placed on tall towers?\nA) Access stronger winds\nB) Reduce land use\nC) Improve aesthetics\nD) Ease of maintenance", "answer": "A"},
    {"question": "What is the purpose of wind resource assessment?\nA) Measure aesthetics\nB) Determine wind energy potential\nC) Assess soil\nD) Calculate noise", "answer": "B"},
    {"question": "What did the 1973 oil crisis accelerate?\nA) Coal use\nB) Wind energy R&D\nC) Nuclear power\nD) Hydropower", "answer": "B"},
    {"question": "Which country installed the first commercial offshore wind farm?\nA) Denmark\nB) USA\nC) China\nD) Germany", "answer": "A"},
    {"question": "What is the primary advantage of using carbon fiber composites in wind turbine blades?\nA) Lower cost\nB) Higher strength-to-weight ratio\nC) Easier manufacturing\nD) Increased flexibility", "answer": "B"},
    {"question": "What aerodynamic phenomenon is mitigated by twisting wind turbine blades along their length?\nA) Tip vortices\nB) Stall at the blade root\nC) Drag divergence\nD) Ground effect", "answer": "B"},
    {"question": "What is the primary purpose of a tapered blade design?\nA) Reduce weight and material costs\nB) Increase noise\nC) Enhance visual appeal\nD) Simplify manufacturing", "answer": "A"},
    {"question": "Which material property is critical for reducing fatigue in wind turbine blades?\nA) High thermal conductivity\nB) High stiffness-to-weight ratio\nC) Electrical conductivity\nD) Magnetic permeability", "answer": "B"},
    {"question": "What role do vortex generators play on wind turbine blades?\nA) Increase drag\nB) Delay flow separation to improve lift\nC) Generate electricity\nD) Reduce icing", "answer": "B"},
    {"question": "What is a key advantage of a doubly-fed induction generator (DFIG)?\nA) Fixed-speed operation\nB) Variable-speed operation with partial-scale converters\nC) No gearbox required\nD) Lower maintenance", "answer": "B"},
    {"question": "Which generator type is most common in direct-drive wind turbines?\nA) Squirrel cage induction\nB) Permanent magnet synchronous\nC) Wound rotor induction\nD) DC generator", "answer": "B"},
    {"question": "What is the function of slip rings in a wound rotor induction generator?\nA) Transfer power to the grid\nB) Allow current to flow to rotor windings\nC) Cool the generator\nD) Control yaw", "answer": "B"},
    {"question": "How do permanent magnet generators differ from induction generators?\nA) Require external DC excitation\nB) Use magnets for field excitation\nC) Lower efficiency\nD) Fixed-speed only", "answer": "B"},
    {"question": "What is a disadvantage of synchronous generators in wind turbines?\nA) Inability to sync with the grid\nB) Brush maintenance\nC) Low torque\nD) High noise", "answer": "B"},
    {"question": "Which technology is best for short-term frequency regulation in wind farms?\nA) Pumped hydro\nB) Flywheels\nC) Lithium-ion batteries\nD) Hydrogen storage", "answer": "B"},
    {"question": "What limits pumped hydro storage for wind energy?\nA) High efficiency\nB) Geographical constraints\nC) Low capacity\nD) Short lifespan", "answer": "B"},
    {"question": "What is the primary use of supercapacitors in wind systems?\nA) Long-term storage\nB) Smoothing rapid power fluctuations\nC) Voltage regulation\nD) Blade heating", "answer": "B"},
    {"question": "Which method stores wind energy as thermal energy?\nA) Batteries\nB) Molten salt systems\nC) Flywheels\nD) Compressed air", "answer": "B"},
    {"question": "What is a challenge for hydrogen storage in wind energy?\nA) Low energy density\nB) High conversion losses\nC) Easy transportation\nD) Abundant infrastructure", "answer": "B"},
    {"question": "Why is HVDC used for offshore wind farms?\nA) Lower cost for short distances\nB) Reduced losses over long distances\nC) Easier installation\nD) Higher AC voltage", "answer": "B"},
    {"question": "What is the role of a step-up transformer in wind farms?\nA) Increase voltage for transmission\nB) Decrease voltage for local use\nC) Convert AC to DC\nD) Store energy", "answer": "A"},
    {"question": "What complicates wind power integration into AC grids?\nA) Intermittency causing frequency fluctuations\nB) Constant output\nC) High inertia\nD) Low voltage", "answer": "A"},
    {"question": "What is 'wind curtailment'?\nA) Reducing wind speed\nB) Reducing output due to grid limits\nC) Increasing efficiency\nD) Storing energy", "answer": "B"},
    {"question": "What is dynamic line rating?\nA) Limiting power flow\nB) Adjusting capacity based on real-time conditions\nC) Increasing voltage\nD) Storing energy", "answer": "B"},
    {"question": "What environmental concern is critical for offshore wind farms?\nA) Air pollution\nB) Marine ecosystem impact\nC) Noise\nD) Visual impact", "answer": "B"},
    {"question": "Why are turbines placed on tall towers?\nA) Access stronger winds\nB) Reduce land use\nC) Improve aesthetics\nD) Ease of maintenance", "answer": "A"},
    {"question": "What is the purpose of wind resource assessment?\nA) Measure aesthetics\nB) Determine wind energy potential\nC) Assess soil\nD) Calculate noise", "answer": "B"},
    {"question": "What did the 1973 oil crisis accelerate?\nA) Coal use\nB) Wind energy R&D\nC) Nuclear power\nD) Hydropower", "answer": "B"},
    {"question": "Which country installed the first commercial offshore wind farm?\nA) Denmark\nB) USA\nC) China\nD) Germany", "answer": "A"},
    {"question": "What is the purpose of a 'bladeless' wind turbine design?\nA) Increase energy output\nB) Reduce mechanical wear and bird collisions\nC) Simplify manufacturing\nD) Enhance aesthetics", "answer": "B"},
    {"question": "How does a swept blade tip improve turbine efficiency?\nA) Reduces tip vortices\nB) Increases blade weight\nC) Lowers rotational speed\nD) Enhances ice resistance", "answer": "A"},
    {"question": "What is 'aeroelastic tailoring' in blade design?\nA) Using rigid materials\nB) Designing blades to bend optimally under wind loads\nC) Reducing blade length\nD) Increasing drag", "answer": "B"},
    {"question": "Why are erosion-resistant coatings applied to blades?\nA) Improve aesthetics\nB) Mitigate damage from rain and sand\nC) Reduce noise\nD) Increase conductivity", "answer": "B"},
    {"question": "What challenge arises from recycling composite wind turbine blades?\nA) High cost of materials\nB) Difficulty separating resins and fibers\nC) Low demand for recycled materials\nD) Toxicity", "answer": "B"},
    {"question": "What is a key benefit of superconducting generators in wind turbines?\nA) Lower material costs\nB) Higher power density and reduced weight\nC) Simpler cooling systems\nD) No need for rare-earth metals", "answer": "B"},
    {"question": "Which generator type is paired with a full-scale converter for grid compatibility?\nA) Squirrel cage induction\nB) Permanent magnet synchronous\nC) Wound rotor induction\nD) DC generator", "answer": "B"},
    {"question": "What is a 'hybrid excitation' generator?\nA) Combines permanent magnets and electromagnets\nB) Uses solar-wind hybrid systems\nC) Requires no cooling\nD) Fixed-speed operation", "answer": "A"},
    {"question": "Why are fault-tolerant generators used in offshore wind turbines?\nA) Lower cost\nB) Improved reliability in harsh environments\nC) Higher speed\nD) Reduced noise", "answer": "B"},
    {"question": "What limits the use of high-temperature superconductors in generators?\nA) High efficiency\nB) Complex cooling requirements\nC) Low power density\nD) Small size", "answer": "B"},
    {"question": "What is 'second-life' battery storage in wind energy systems?\nA) Reusing retired EV batteries\nB) Doubling battery capacity\nC) Recycling lithium\nD) Reducing charge cycles", "answer": "A"},
    {"question": "Which storage method uses compressed air in underground caverns?\nA) CAES\nB) VRFB\nC) Flywheel\nD) Lithium-ion", "answer": "A"},
    {"question": "What is a drawback of gravity-based energy storage for wind power?\nA) Low energy density\nB) High geographical dependency\nC) Slow response time\nD) Toxicity", "answer": "B"},
    {"question": "What role do redox flow batteries play in seasonal wind energy storage?\nA) Short-term frequency regulation\nB) Long-duration energy storage\nC) Blade heating\nD) Grid-forming support", "answer": "B"},
    {"question": "Why are hybrid storage systems (e.g., battery + flywheel) used with wind farms?\nA) Combine high power and energy density\nB) Reduce costs\nC) Simplify maintenance\nD) Increase land use", "answer": "A"},
    {"question": "What is a 'synchrophasor' in wind farm grid management?\nA) A turbine component\nB) A device measuring grid voltage/phase in real time\nC) A type of transformer\nD) A battery system", "answer": "B"},
    {"question": "Why are submarine cables critical for offshore wind farms?\nA) Transmit power to shore\nB) Anchor turbines\nC) Cool generators\nD) Measure wind speed", "answer": "A"},
    {"question": "What is 'black start' capability in wind turbines?\nA) Restarting the grid without external power\nB) Reducing blade speed\nC) Storing energy\nD) Cooling systems", "answer": "A"},
    {"question": "What is the role of phase-shifting transformers in wind power integration?\nA) Control power flow between grids\nB) Increase voltage\nC) Store energy\nD) Reduce noise", "answer": "A"},
    {"question": "What cybersecurity risks affect wind farm transmission systems?\nA) Physical theft\nB) Hacking SCADA systems\nC) Blade erosion\nD) Generator overheating", "answer": "B"},
    {"question": "Why are LiDAR systems used in wind resource assessment?\nA) Measure wind speed at multiple heights\nB) Track bird migration\nC) Inspect blade surfaces\nD) Cool turbines", "answer": "A"},
    {"question": "What is 'micrositing' in wind farm planning?\nA) Optimizing turbine placement for maximum yield\nB) Reducing turbine size\nC) Installing small turbines\nD) Landscaping", "answer": "A"},
    {"question": "What environmental study is critical before offshore wind farm construction?\nA) Bird and marine life impact assessments\nB) Air quality testing\nC) Soil erosion analysis\nD) Noise mapping", "answer": "A"},
    {"question": "What is a 'floating' offshore wind turbine foundation?\nA) Anchored to the seabed with tension legs\nB) Fixed to the ocean floor\nC) A submerged platform\nD) A ship-based turbine", "answer": "A"},
    {"question": "Which ancient civilization used windmills for grinding grain?\nA) Persians\nB) Romans\nC) Egyptians\nD) Chinese", "answer": "A"},
    {"question": "What breakthrough in the 1980s enabled modern multi-megawatt turbines?\nA) Fiberglass blades\nB) Variable-speed generators\nC) Steel towers\nD) Hydraulic pitch control", "answer": "A"},
    {"question": "Which wind farm was the first to exceed 1 GW capacity?\nA) Hornsea One (UK)\nB) Alta Wind (USA)\nC) Gansu (China)\nD) London Array (UK)", "answer": "A"},
    {"question": "What is the function of a winglet on a wind turbine blade?\nA) Reduces noise emission\nB) Decreases mechanical stress\nC) Improves aerodynamic efficiency by reducing tip vortices\nD) Prevents ice formation", "answer": "C"},
    {"question": "Why are modern wind turbine blades twisted along their length?\nA) To reduce manufacturing costs\nB) To maintain optimal angle of attack at different radial positions\nC) To improve structural integrity\nD) To minimize lightning strikes", "answer": "B"},
    {"question": "What material innovation has allowed for longer wind turbine blades?\nA) Aluminum alloys\nB) Carbon fiber composites\nC) Titanium reinforcement\nD) Ceramic coatings", "answer": "B"},
    {"question": "What is 'pitch control' in wind turbine blade systems?\nA) Changing blade angle to optimize energy capture or limit output\nB) Altering the sound frequency of blade movement\nC) Controlling the distance between turbines\nD) Adjusting tower height", "answer": "A"},
    {"question": "What advantage do direct-drive generators offer over geared systems?\nA) Higher rotational speeds\nB) Lower maintenance requirements\nC) Reduced power output\nD) Smaller diameter", "answer": "B"},
    {"question": "Which cooling method is commonly used in large wind turbine generators?\nA) Liquid nitrogen\nB) Forced air cooling\nC) Helium circulation\nD) Phase-change materials", "answer": "B"},
    {"question": "What is the function of a slip ring in a doubly-fed induction generator?\nA) Transferring power to the rotating rotor windings\nB) Connecting the nacelle to the tower\nC) Measuring wind speed\nD) Filtering DC current", "answer": "A"},
    {"question": "Why are rare-earth elements important in permanent magnet generators?\nA) They reduce overall weight\nB) They create stronger magnetic fields\nC) They improve cooling efficiency\nD) They eliminate the need for maintenance", "answer": "B"},
    {"question": "What is the main purpose of hydrogen storage in wind energy systems?\nA) Short-term frequency regulation\nB) Long-duration seasonal storage\nC) Emergency backup power\nD) Blade deicing", "answer": "B"},
    {"question": "Which energy storage technology has the highest round-trip efficiency?\nA) Pumped hydro storage\nB) Hydrogen fuel cells\nC) Lithium-ion batteries\nD) Compressed air energy storage", "answer": "C"},
    {"question": "What is 'power-to-gas' in wind energy storage systems?\nA) Using excess electricity to produce hydrogen or methane\nB) Converting natural gas to electricity\nC) Pressurizing gas turbines\nD) Liquefying air for storage", "answer": "A"},
    {"question": "What benefit do thermal energy storage systems provide to wind farms?\nA) Generator cooling\nB) Blade deicing\nC) Low-cost long-duration storage\nD) Improved grid reliability", "answer": "C"},
    {"question": "What is 'dynamic line rating' in wind farm transmission?\nA) Variable pricing for wind power\nB) Real-time assessment of transmission line capacity\nC) Changing voltage levels based on demand\nD) Automatic fault detection", "answer": "B"},
    {"question": "Why are HVDC (High Voltage Direct Current) connections used for distant offshore wind farms?\nA) Lower transmission losses over long distances\nB) Simpler converter stations\nC) Reduced cable costs\nD) Higher reliability in storms", "answer": "A"},
    {"question": "What grid service can wind farms with fast-responding inverters provide?\nA) Baseload power\nB) Synthetic inertia\nC) Peak load generation\nD) Carbon capture", "answer": "B"},
    {"question": "What is 'curtailment' in wind power grid management?\nA) Reducing output below available capacity due to grid constraints\nB) Cutting transmission lines during storms\nC) Shutting down for maintenance\nD) Limiting noise during night hours", "answer": "A"},
    {"question": "What is a 'wake effect' in wind farm layout planning?\nA) Noise pattern caused by blade movement\nB) Reduced wind speed downwind of turbines\nC) Visual impact on landscapes\nD) Thermal gradient created by turbines", "answer": "B"},
    {"question": "Why is bathymetry crucial for offshore wind site selection?\nA) To determine seabed depth and features for foundation design\nB) To assess fish migration patterns\nC) To measure tidal energy potential\nD) To evaluate shipping lanes", "answer": "A"},
    {"question": "What analysis predicts noise propagation from wind farms?\nA) Electromagnetic compatibility study\nB) Acoustic modeling\nC) Visual impact assessment\nD) Grid stability analysis", "answer": "B"},
    {"question": "What is 'repowering' in wind farm management?\nA) Restarting after grid failure\nB) Replacing older turbines with newer, more efficient models\nC) Increasing transmission capacity\nD) Changing ownership structure", "answer": "B"},
    {"question": "Who is credited with inventing the first electricity-generating wind turbine in 1887?\nA) Thomas Edison\nB) Nikola Tesla\nC) James Blyth\nD) Charles Brush", "answer": "C"},
    {"question": "Which country built the world's first offshore wind farm in 1991?\nA) United States\nB) United Kingdom\nC) Denmark\nD) Germany", "answer": "C"},
    {"question": "What was the primary function of windmills in the Netherlands historically?\nA) Grinding grain\nB) Pumping water for land drainage\nC) Sawing timber\nD) Generating electricity", "answer": "B"},
    {"question": "Which innovation from the aerospace industry significantly influenced modern wind turbine design?\nA) Composite materials\nB) Hydraulic systems\nC) Airfoil profiles\nD) All of the above", "answer": "D"}
]

def calculate_summary_stats(score, total_questions, answered_count, elapsed_time):
    percentage_correct = (score / total_questions) * 100 if total_questions > 0 else 0
    avg_time_per_question = elapsed_time / answered_count if answered_count > 0 else 0
    return {
        "Total Score": f"{score} / {total_questions}",
        "Percentage Correct": f"{percentage_correct:.2f}%",
        "Questions Answered": answered_count,
        "Average Time per Question": f"{avg_time_per_question:.2f} seconds"
    }

def main():
    st.title("Wind Power Quiz")
    st.write("Answer 25 questions in 20 minutes. Good luck!")

    # Custom CSS for timer positioning
    st.markdown("""
        <style>
        .timer {
            position: fixed;
            top: 10px;
            right: 10px;
            font-size: 18px;
            font-weight: bold;
            color: #ff4b4b;
            background-color: #f0f0f0;
            padding: 5px 10px;
            border-radius: 5px;
            z-index: 999;
        }
        </style>
    """, unsafe_allow_html=True)

    # Initialize session state
    if 'start_time' not in st.session_state:
        st.session_state.start_time = time.time()
    if 'question_list' not in st.session_state:
        st.session_state.question_list = random.sample(QUESTIONS, 25)
    if 'question_index' not in st.session_state:
        st.session_state.question_index = 0
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'user_answers' not in st.session_state:
        st.session_state.user_answers = []
    if 'answered' not in st.session_state:
        st.session_state.answered = [False] * 25

    # Timer (20 minutes = 1200 seconds)
    elapsed_time = time.time() - st.session_state.start_time
    time_left = max(1200 - elapsed_time, 0)
    st.write(f"Time Left: {int(time_left)} seconds")

    # Check if time is up
    if time_left <= 0:
        st.error("Time's up!")
        st.write(f"Final Score: {st.session_state.score} / 25")
        answered_count = sum(1 for ans in st.session_state.answered if ans)
        stats = calculate_summary_stats(st.session_state.score, 25, answered_count, elapsed_time)
        st.subheader("Summary Statistics")
        for key, value in stats.items():
            st.write(f"{key}: {value}")
        return

    # Progress bar
    st.progress(st.session_state.question_index / 25)

    # Current question
    if st.session_state.question_index < 25:
        current_q = st.session_state.question_list[st.session_state.question_index]
        st.subheader(f"Question {st.session_state.question_index + 1}")
        st.write(current_q["question"])
        options = current_q["question"].split('\n')[1:]  # Extract options
        user_answer = st.radio("Select an option:", options, key=f"q_{st.session_state.question_index}")

        # Submit button
        if st.button("Submit Answer") and not st.session_state.answered[st.session_state.question_index]:
            correct_answer = current_q["answer"]
            st.session_state.answered[st.session_state.question_index] = True
            user_answer_letter = user_answer.split(')')[0].replace(' ', '')  # Extract letter (e.g., "A")
            st.session_state.user_answers.append(user_answer_letter)
            if user_answer_letter == correct_answer:
                st.session_state.score += 1
                st.success("Correct!")
            else:
                st.error(f"Incorrect. The correct answer is {correct_answer}.")
            st.write(f"Current Score: {st.session_state.score} / {st.session_state.question_index + 1}")

        # Next button
        if st.button("Next Question") and st.session_state.answered[st.session_state.question_index]:
            if st.session_state.question_index < 24:
                st.session_state.question_index += 1
                st.rerun()
            else:
                st.success("Quiz completed!")
                st.write(f"Final Score: {st.session_state.score} / 25")
                answered_count = sum(1 for ans in st.session_state.answered if ans)
                stats = calculate_summary_stats(st.session_state.score, 25, answered_count, elapsed_time)
                st.subheader("Summary Statistics")
                for key, value in stats.items():
                    st.write(f"{key}: {value}")
    else:
        st.success("Quiz completed!")
        st.write(f"Final Score: {st.session_state.score} / 25")
        answered_count = sum(1 for ans in st.session_state.answered if ans)
        stats = calculate_summary_stats(st.session_state.score, 25, answered_count, elapsed_time)
        st.subheader("Summary Statistics")
        for key, value in stats.items():
            st.write(f"{key}: {value}")

if __name__ == "__main__":
    main()