import pytest
from app.services.ai_service import summarize_note


def test_summarize_note(mocker):
    """
    Test for summarize_note function using mocks.
    """
    mock_model = mocker.MagicMock()
    mock_model.generate_content.return_value.text = "This is a mock summary."
    mocker.patch("google.generativeai.GenerativeModel", return_value=mock_model)

    content = """
    Software testing is a crucial phase in the development lifecycle, ensuring that applications function as expected and meet quality standards. It involves verifying and validating software to detect bugs, security vulnerabilities, and performance issues before deployment.
    There are various types of testing, including unit testing, integration testing, system testing, and acceptance testing. Unit testing focuses on individual components, while integration testing checks how different modules work together. System testing evaluates the complete application, and acceptance testing determines if the product meets user requirements.
    Automated testing tools like Selenium, PyTest, and JUnit help streamline the process, reducing manual effort and improving efficiency. Additionally, continuous testing in DevOps ensures that code changes do not introduce new defects.
    Ultimately, thorough testing improves software reliability, enhances user experience, and reduces maintenance costs, making it an essential practice in modern software development.
    """
    summary = summarize_note(content)

    assert summary == "This is a mock summary."
    mock_model.generate_content.assert_called_once_with(f"Summarize this note: {content}")


def test_summarize_note_empty_content(mocker):
    """
    Test for summarize_note function with empty content.
    """
    mock_model = mocker.MagicMock()
    mock_model.generate_content.return_value.text = "This is a mock summary."
    mocker.patch("google.generativeai.GenerativeModel", return_value=mock_model)

    content = ""
    summary = summarize_note(content)

    assert summary == "This is a mock summary."
    mock_model.generate_content.assert_called_once_with(f"Summarize this note: {content}")


def test_summarize_note_error_handling(mocker):
    """
    Test for summarize_note function to ensure error handling.
    """
    mock_model = mocker.MagicMock()
    mock_model.generate_content.side_effect = Exception("Mock error")
    mocker.patch("google.generativeai.GenerativeModel", return_value=mock_model)

    content = """
    Software testing is a crucial phase in the development lifecycle, ensuring that applications function as expected and meet quality standards. It involves verifying and validating software to detect bugs, security vulnerabilities, and performance issues before deployment.
    """
    with pytest.raises(Exception) as exc_info:
        summarize_note(content)

    assert str(exc_info.value) == "Mock error"
    mock_model.generate_content.assert_called_once_with(f"Summarize this note: {content}")