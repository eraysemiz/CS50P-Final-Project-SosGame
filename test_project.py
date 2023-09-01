import pytest
from project import *


def test_get_move(capsys):
    sos = SosGame()
    with pytest.raises(SystemExit):
        sos.get_move("exit")
    with pytest.raises(SystemExit):
        sos.get_move("endgame")

    sos.get_move("Z9", test_=1)
    captured_print = capsys.readouterr()
    expected_print = "\x1b[35mPlease structure your input using letters from A to F and numbers from 1 to 6.\n"
    assert expected_print in captured_print


def test_get_letter(capsys):
    sos = SosGame()
    sos.get_letter("H", "A1", test_=1)
    captured_print = capsys.readouterr()
    expected_print = '\x1b[35mInvalid letter.\n'
    assert expected_print in captured_print


def test_play():
    sos = SosGame()
    sos.play("A2", "O", test_=1)
    assert sos.cells["A2"] == "| O |"


def test_score_table():
    sos = SosGame()
    sos.score_table("Player1")
    assert sos.player1_score == 1


def test_score():
    sos = SosGame()
    sos.cells["A2"] = "| S |"
    sos.cells["A3"] = "| O |"
    sos.cells["A4"] = "| S |"
    sos.score("Player2")
    assert sos.player2_score == 1


def test_endgame():
    sos = SosGame()
    sos.empty_spaces = 0
    with pytest.raises(SystemExit):
        sos.end_game()


def test_exit_game():
    sos = SosGame()
    with pytest.raises(SystemExit):
        sos.exit_game("CS50")
