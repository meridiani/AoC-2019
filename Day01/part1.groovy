
// take input file
// calculate fuel total for eahc line
// sum the totals


// Fuel required to launch a given module is based on its mass. 
// Specifically, to find the fuel required for a module, 
// take its mass, 
// divide by three, 
// round down, 
// and subtract 2.

//---------------------------------------------------------------------------//

Integer fuelForLaunch(mass)
  fuel = round(mass/3) - 2

  return fuel


//---------------------------------------------------------------------------//
println 'OK to go!'
