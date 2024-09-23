Fixture

@pytest.fixture()

def setup():
  print("This will execute first")
  yield #this will execute at last 
  ("This will execute at last")

def test_fixturedemo():
  print("This will execute after setup")
