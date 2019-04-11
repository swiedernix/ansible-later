"""Test logging module."""

from __future__ import print_function

import colorama

from ansiblelater import logger


def test_critical(capsys, mocker):
    log = logger.get_logger("test_critical")
    log.critical("foo")
    _, stderr = capsys.readouterr()

    print("{}{}{}".format(colorama.Fore.RED, "CRITICAL: foo".rstrip(),
                          colorama.Style.RESET_ALL))
    x, _ = capsys.readouterr()

    assert x == stderr


def test_error(capsys, mocker):
    log = logger.get_logger("test_error")
    log.error("foo")
    _, stderr = capsys.readouterr()

    print("{}{}{}".format(colorama.Fore.RED, "ERROR: foo".rstrip(),
                          colorama.Style.RESET_ALL))
    x, _ = capsys.readouterr()

    assert x == stderr


def test_warn(capsys, mocker):
    log = logger.get_logger("test_warn")
    log.warning("foo")
    stdout, _ = capsys.readouterr()

    print("{}{}{}".format(colorama.Fore.YELLOW, "WARNING: foo".rstrip(),
                          colorama.Style.RESET_ALL))
    x, _ = capsys.readouterr()

    assert x == stdout


def test_info(capsys, mocker):
    log = logger.get_logger("test_info")
    log.info("foo")
    stdout, _ = capsys.readouterr()

    print("{}{}{}".format(colorama.Fore.BLUE, "INFO: foo".rstrip(),
                          colorama.Style.RESET_ALL))
    x, _ = capsys.readouterr()

    assert x == stdout


def test_markup_detection_pycolors0(monkeypatch):
    monkeypatch.setenv("PY_COLORS", "0")
    assert not logger._should_do_markup()


def test_markup_detection_pycolors1(monkeypatch):
    monkeypatch.setenv("PY_COLORS", "1")
    assert logger._should_do_markup()


def test_markup_detection_tty_yes(mocker):
    mocker.patch("sys.stdout.isatty", return_value=True)
    mocker.patch("os.environ", {"TERM": "xterm"})
    assert logger._should_do_markup()
    mocker.resetall()
    mocker.stopall()


def test_markup_detection_tty_no(mocker):
    mocker.patch("os.environ", {})
    mocker.patch("sys.stdout.isatty", return_value=False)
    assert not logger._should_do_markup()
    mocker.resetall()
    mocker.stopall()
