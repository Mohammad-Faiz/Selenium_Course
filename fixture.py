Fixture


@pytest.fixture()
def setup():
  print("This will execute first")
  yield 
  print("This will execute at last")
"""ABOVE FUNCTION PUT IN ANOTHER PAGE"""




def test_fixturedemo():
  print("This will execute after setup")

def test_fixturedemo1():
  print("This will execute after setup2")
  
def test_fixturedemo2():
  print("This will execute after setup3")

FOR ABOVE CODE WE WILL GET OUTPUT: - 
This will execute first
This will execute after setup
This will execute at last


IF WE CHANGE 
def setup(scope = "class"):
  print("This will execute first")
  yield 
  print("This will execute at last")
#now at the beggining of test test setup will run and at last of the all test yield will run
