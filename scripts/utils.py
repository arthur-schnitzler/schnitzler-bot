from datetime import datetime
from acdh_tei_pyutils.tei import TeiReader
from acdh_tei_pyutils.utils import extract_fulltext

from config import DATA_URL


def current_day() -> str:
    """Returns the current date in 'MM-DD' format.
    Uses datetime.now() to get the current date and formats it using strftime.
    The function returns a string representation of the current month and day,
    separated by a hyphen.
    Returns:
        str: Current date formatted as 'MM-DD' (e.g., '01-25' for January 25th)
    """
    return datetime.now().strftime("%m-%d")


def years_ago(year: str) -> str:
    """Calculate the number of years between a given year and the current year.
    Args:
        year (str): The year to calculate the difference from, as a string.
    Returns:
        int: The difference between the current year and the input year.
    Example:
        >>> years_ago('1990')
        33  # if current year is 2023
    """

    this_year = int(datetime.now().strftime("%Y"))
    year = int(year)
    return this_year - year


def get_schnitzler_date(before_how_many_years=125) -> str:
    """
    Calculate a date that is a specified number of years before the current date.
    Args:
        before_how_many_years (int, optional): The number of years to subtract from the current year. Defaults to 125.
    Returns:
        str: A string representing the calculated date in the format "YYYY-MM-DD".
    """
    current_date = datetime.now().strftime("%Y-%m-%d")
    year = datetime.now().year
    schnitzler_year = year - before_how_many_years
    schnitzler_day = "-".join(current_date.split("-")[1:])
    schnitzler_date = f"{schnitzler_year}-{schnitzler_day}"
    return schnitzler_date


def get_xml(before_how_many_years=125) -> TeiReader:
    """
    Fetches and returns an XML document from a specified URL.
    Args:
        before_how_many_years (int, optional): The number of years before the current date to calculate the target date. Defaults to 125.
    Returns:
        TeiReader: An instance of TeiReader containing the XML document from the constructed URL.
    """  # noqa: E501

    url = f"{DATA_URL}{get_schnitzler_date(before_how_many_years)}.xml"
    return TeiReader(url)


def get_text(before_how_many_years=125, max_length=250) -> str:
    """
    Retrieve and extract a portion of text from an XML document.
    Args:
        before_how_many_years (int, optional): The number of years before the current date to filter the XML document. Defaults to 125.
        max_length (int, optional): The maximum length of the extracted text. Defaults to 200.
    Returns:
        str: A string containing the extracted text, truncated to the specified maximum length.
    """  # noqa: E501

    doc = get_xml(before_how_many_years)
    text = extract_fulltext(doc.any_xpath(".//tei:div[@type='diary-day']")[0])
    if len(text) > max_length:
        return f"{text[:max_length]} ..."
    else:
        return text
