def execute_code(code):
    """사용자가 입력한 코드를 실행하고 결과를 반환한다."""
    try:
        exec_globals = {}
        exec(code, exec_globals)
        return exec_globals
    except Exception as e:
        return str(e)

