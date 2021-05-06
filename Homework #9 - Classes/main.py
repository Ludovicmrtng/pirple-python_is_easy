class Vehicle:
  def __init__(self,make,model,year,weight):
    self.make = make
    self.model = model
    self.year = year
    self.weight = weight
    self.needsMaintenance = False
    self.tripSinceMaintenance = 0
  
  def Repair(self):
    self.tripSinceMaintenance = 0
    self.needsMaintenance = False

class Cars(Vehicle):
  def __init__(self,mk,md,yr,wght):
    Vehicle.__init__(self,mk,md,yr,wght)
    self.isDriving = False
  
  def Drive(self):
    self.isDriving = True
  
  def Stop(self):
    if self.isDriving:
      self.tripSinceMaintenance += 1
      if self.tripSinceMaintenance > 100:
        self.needsMaintenance = True
    self.isDriving = False

class Planes(Vehicle):
  def __init__(self,mk,md,yr,wght):
    Vehicle.__init__(self,mk,md,yr,wght)
    self.isFlying = False
  
  def Fly(self):
    self.isFlying = True
  
  def Land(self):
    if self.isFlying:
      self.tripSinceMaintenance += 1
      if self.tripSinceMaintenance > 100:
        self.needsMaintenance = True
    self.isFlying = False

def driveCounter(car,driveTimes):
  for i in range(1,driveTimes + 1):
    car.Drive()
    car.Stop()

def flyCounter(plane,flyTimes):
  for i in range(1,flyTimes + 1):
    plane.Fly()
    plane.Land()

#Showing the specifications of the vehicle
def ShowSpecs(vehicle):
  print("---------------------")
  print("Make:",vehicle.make)
  print("Model:",vehicle.model)
  print("Year:",vehicle.year)
  print("Weight:",vehicle.weight)
  print("Needs Maintenance:",vehicle.needsMaintenance)
  print("Trip Since Maintenance:",vehicle.tripSinceMaintenance)
  print("---------------------")

def goOnRepairMode(car):
  if car.tripSinceMaintenance > 100:
    car.Repair()
    print(car.make,"is on RepairMode")
  else:
    leftKm = 100 - car.tripSinceMaintenance
    print(car.make,f"has {leftKm} left before maintenance")

#If plane try to fly if it's on maintenance
def attemptToFly(plane):
  if plane.needsMaintenance == True:
    plane.isFlying = False
    print(plane.make,"can't fly until it's repaired.")
  else:
    leftKms = 100 - plane.tripSinceMaintenance
    print(plane.make,f"has {leftKms} to fly")


car1 = Cars("Mercedes","AMG",2020,2250)
car2 = Cars("BMW","320i",2005,3010)
car3 = Cars("Audi","A4",2013,2050)

plane1 = Planes("Emirates","A380",2015,23000)
plane2 = Planes("BritishAirways","A347",2012,30000)
plane3 = Planes("AirFrance","Boeing777",2010,45000)

driveCounter(car1,105)
driveCounter(car2,80)
driveCounter(car3,32)

flyCounter(plane1,204)
flyCounter(plane2,97)
flyCounter(plane3,135)

ShowSpecs(car1)
ShowSpecs(car2)
ShowSpecs(car3)

goOnRepairMode(car1)
goOnRepairMode(car2)
goOnRepairMode(car3)

ShowSpecs(plane1)
ShowSpecs(plane2)
ShowSpecs(plane3)

attemptToFly(plane1)
attemptToFly(plane2)
attemptToFly(plane3)



