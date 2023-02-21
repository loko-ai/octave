import oct2py
from flask import Flask, request, jsonify
from loguru import logger
from loko_extensions.business.decorators import extract_value_args
from loko_extensions.model.components import Component, save_extensions, Arg
import numpy as np

app = Flask("octave")
c = Component("Octave", group="Scripting", args=[Arg("code", type="code", value="ret=linspace(0, 2*pi)")],
              description="""This components allows to run octave/matlab code. The return value has to be assigned to the 'ret' variable""")

save_extensions([c])

octave = oct2py.Oct2Py()


def json_response(o):
    if isinstance(o, np.ndarray):
        return o.tolist()
    else:
        return o


@app.route("/", methods=["POST"])
@extract_value_args(_request=request)
def execute(value, args):
    code = args.get("code")
    fcode = f"""function ret=secretfunctionname()
      {code}
    endfunction
    secretfunctionname()
    """
    logger.debug(fcode)
    result = octave.eval(fcode)

    return jsonify(json_response(result))


if __name__ == "__main__":
    app.run("0.0.0.0", 8080)
