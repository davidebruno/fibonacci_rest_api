from flask import Flask
from flask_restful import abort, Api, Resource
from fibonacci import fibonacci_calc, MAX_FIBONACCI_VALUE

app = Flask(__name__)
api = Api(app)


'''
    The following method verify the input parameters passed as argument and returns the appropriate message
'''
def abort_if_parameter_exceeds_max_value(id):
    try:
        val = int(id)
    except:
        abort(500, message="The requested value is: {} please note that only zero or positive integers are valid fibonacci's domain values ".format(id))
    if val < 0:
        abort(500, message="The value requested is {} but only zero or positive integers are valid fibonacci's domain values ".format(id))
    if val > MAX_FIBONACCI_VALUE:
        abort(500, message="The value of {} is exceeding the max value allowed of {} ".format(id, MAX_FIBONACCI_VALUE))

# parser = reqparse.RequestParser()

# Fib
# returns the Fibonacci list of values calculated for the passed parameter
class Fib(Resource):
    def get(self, id):
        abort_if_parameter_exceeds_max_value(id)
        return fibonacci_calc(id)


api.add_resource(Fib, '/fibonacci/<string:id>')


if __name__ == '__main__':
    app.run(debug=True)