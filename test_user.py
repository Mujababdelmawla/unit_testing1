from user import User

def test_user_profile_contains_name():
    #Arrange
    user = User(name="Mujab")
    # Act 
    result = user.get_profile()
    # Assert
    assert "Mujab" in result

def test_user_profile_empty_name():
    #Arrange
    user = User(name="")
    #Act 
    result = user.get_profile()
    #Assert
    assert "user profile: " in result

def test_user_profile_long_name():
    #Arrange
    long_name = "A" * 100
    user = User(name=long_name)
    #Act
    result = user.get_profile()
    #Assert
    assert long_name in result
