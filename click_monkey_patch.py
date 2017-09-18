def prevent_ascii_env():
    """
    To avoid issues reading unicode chars from stdin or writing to stdout, we need to ensure that the
    python3 runtime is correctly configured, if not, we try to force to utf-8,
    but It isn't possible then we exit with a more friendly message that the original one.
    """
    import locale, codecs, os, sys
    # locale.getpreferredencoding() == 'ANSI_X3.4-1968'
    if codecs.lookup(locale.getpreferredencoding()).name == 'ascii':
        os.environ['LANG'] = 'en_US.utf-8'
        if codecs.lookup(locale.getpreferredencoding()).name == 'ascii':
            print("The current locale is not correctly configured in your system")
            print("Please set the LANG env variable to the proper value before to call this script")
            sys.exit(-1)
        #Once we have the proper locale.getpreferredencoding() We can change current stdin/out streams
        _, encoding = locale.getdefaultlocale()
        import io
        sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding=encoding, errors="replace", line_buffering=True)
        sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding=encoding, errors="replace", line_buffering=True)
        sys.stdin = io.TextIOWrapper(sys.stdin.detach(), encoding=encoding, errors="replace", line_buffering=True)
        # And finally we need to re-encode the input parameters
        for i, p in enumerate(sys.argv):
            sys.argv[i] = os.fsencode(p).decode()

def wrapper_get_terminal_size():
    """
    Replace the original function termui.get_terminal_size (click lib) by a new one
    that uses a fallback if ValueError exception has been raised
    """
    from click import termui, formatting

    old_get_term_size = termui.get_terminal_size
    def _wrapped_get_terminal_size():
        try:
            return old_get_term_size()
        except ValueError:
            import os
            sz = os.get_terminal_size()
            return sz.columns, sz.lines
    termui.get_terminal_size = _wrapped_get_terminal_size
    formatting.get_terminal_size = _wrapped_get_terminal_size