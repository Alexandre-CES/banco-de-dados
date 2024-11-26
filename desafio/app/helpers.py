from flask import jsonify

def format_multipolygon(coordinates):
    """Format MultiPolygon coordinates to WKT."""
    return ", ".join(
        f"(({', '.join(f'{point[0]} {point[1]}' for point in ring)}))"
        for ring in coordinates[0]
    )


def format_error(message, details=None, code=400):
    """Format an error message."""
    response = {"error": message}
    if details:
        response["details"] = details
    return jsonify(response), code
