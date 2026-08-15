import json

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt


DEALERS = [
    {
        "id": 1,
        "full_name": "Best Cars Dealership",
        "city": "Wichita",
        "state": "Kansas",
        "address": "123 Main Street"
    },
    {
        "id": 2,
        "full_name": "Premium Auto Center",
        "city": "Kansas City",
        "state": "Kansas",
        "address": "456 Auto Avenue"
    },
    {
        "id": 3,
        "full_name": "Quality Motors",
        "city": "Dallas",
        "state": "Texas",
        "address": "789 Motor Road"
    }
]


def home(request):
    state = request.GET.get("state", "")

    dealers = DEALERS

    if state:
        dealers = [
            dealer for dealer in DEALERS
            if dealer["state"].lower() == state.lower()
        ]

    if request.user.is_authenticated:
        user_section = f"""
            <span>Welcome, <strong>{request.user.username}</strong></span>
            <a href="/djangoapp/logout">Logout</a>
        """
        review_button = """
            <a class="review-btn" href="/dealer/1/post-review">
                Review Dealer
            </a>
        """
    else:
        user_section = '<a href="/admin/login/">Login</a>'
        review_button = ""

    dealer_cards = ""

    for dealer in dealers:
        dealer_cards += f"""
        <div class="dealer-card">
            <h2>{dealer["full_name"]}</h2>
            <p><strong>City:</strong> {dealer["city"]}</p>
            <p><strong>State:</strong> {dealer["state"]}</p>
            <p><strong>Address:</strong> {dealer["address"]}</p>
            {review_button}
        </div>
        """

    html = f"""
    <html>
    <head>
        <title>Cars Dealership</title>
        <style>
            body {{
                font-family: Arial;
                background: #f5f5f5;
                margin: 0;
            }}
            nav {{
                background: #222;
                color: white;
                padding: 15px 30px;
                display: flex;
                justify-content: space-between;
            }}
            nav a {{
                color: white;
                margin-left: 20px;
                text-decoration: none;
            }}
            .container {{
                width: 90%;
                margin: 30px auto;
            }}
            .dealer-card {{
                background: white;
                padding: 20px;
                margin-bottom: 20px;
                border-radius: 10px;
            }}
            .review-btn {{
                display: inline-block;
                background: #0d6efd;
                color: white;
                padding: 10px 15px;
                border-radius: 5px;
                text-decoration: none;
            }}
        </style>
    </head>

    <body>
        <nav>
            <strong>Cars Dealership</strong>
            <div>
                <a href="/">Home</a>
                {user_section}
            </div>
        </nav>

        <div class="container">

            <h1>Available Car Dealerships</h1>

            <form method="GET">
                <label>Filter by State:</label>

                <select name="state">
                    <option value="">All States</option>
                    <option value="Kansas">Kansas</option>
                    <option value="Texas">Texas</option>
                </select>

                <button type="submit">Filter</button>
            </form>

            {dealer_cards}

        </div>
    </body>
    </html>
    """

    return HttpResponse(html)


@csrf_exempt
def login_user(request):
    if request.method != "POST":
        return JsonResponse(
            {"error": "POST request required"},
            status=405
        )

    data = json.loads(request.body)

    username = data.get("userName")
    password = data.get("password")

    user = authenticate(
        request,
        username=username,
        password=password
    )

    if user is not None:
        login(request, user)

        return JsonResponse({
            "status": "Authenticated",
            "userName": username
        })

    return JsonResponse(
        {
            "status": "Failed",
            "message": "Invalid credentials"
        },
        status=401
    )


def logout_user(request):
    logout(request)

    return JsonResponse({
        "status": "Logged out"
    })


def get_dealer_reviews(request, dealer_id):
    reviews = [
        {
            "dealer_id": dealer_id,
            "reviewer": "Sandhiya",
            "rating": 5,
            "review": "Excellent service and friendly staff."
        },
        {
            "dealer_id": dealer_id,
            "reviewer": "Arun",
            "rating": 4,
            "review": "Good dealership experience."
        }
    ]

    return JsonResponse(reviews, safe=False)


def get_all_dealers(request):
    return JsonResponse(DEALERS, safe=False)


def get_dealer_by_id(request, dealer_id):
    dealer = next(
        (d for d in DEALERS if d["id"] == dealer_id),
        None
    )

    if dealer is None:
        return JsonResponse(
            {"error": "Dealer not found"},
            status=404
        )

    return JsonResponse(dealer)


def get_dealers_by_state(request, state):
    dealers = [
        d for d in DEALERS
        if d["state"].lower() == state.lower()
    ]

    return JsonResponse(dealers, safe=False)


def get_all_car_makes(request):
    car_makes = [
        {
            "make": "Toyota",
            "models": ["Camry", "Corolla", "RAV4"]
        },
        {
            "make": "Honda",
            "models": ["Civic", "Accord", "CR-V"]
        },
        {
            "make": "Ford",
            "models": ["Mustang", "Explorer", "F-150"]
        }
    ]

    return JsonResponse(car_makes, safe=False)


def analyze_review(request):
    review_text = request.GET.get("text", "")

    sentiment = (
        "positive"
        if "fantastic" in review_text.lower()
        else "neutral"
    )

    return JsonResponse({
        "review": review_text,
        "sentiment": sentiment
    })


def dealer_details_reviews(request, dealer_id):
    dealer = next(
        (d for d in DEALERS if d["id"] == dealer_id),
        None
    )

    if dealer is None:
        return HttpResponse("Dealer not found", status=404)

    html = f"""
    <html>
    <head>
        <title>Dealer Details</title>
    </head>

    <body style="font-family:Arial;background:#f5f5f5">

        <h1>Dealer Details</h1>

        <div style="background:white;padding:25px;margin:20px">
            <h2>{dealer["full_name"]}</h2>
            <p>Dealer ID: {dealer["id"]}</p>
            <p>City: {dealer["city"]}</p>
            <p>State: {dealer["state"]}</p>
            <p>Address: {dealer["address"]}</p>
        </div>

        <h2>Customer Reviews</h2>

        <div style="background:white;padding:20px;margin:20px">
            <h3>Sandhiya</h3>
            <p>Rating: 5/5</p>
            <p>Excellent service and friendly staff.</p>
        </div>

        <div style="background:white;padding:20px;margin:20px">
            <h3>Arun</h3>
            <p>Rating: 4/5</p>
            <p>Good dealership experience.</p>
        </div>

    </body>
    </html>
    """

    return HttpResponse(html)


@csrf_exempt
def post_review_page(request, dealer_id):
    dealer = next(
        (d for d in DEALERS if d["id"] == dealer_id),
        None
    )

    if dealer is None:
        return HttpResponse("Dealer not found", status=404)

    if request.method == "POST":
        reviewer = request.POST.get("reviewer", "")
        rating = request.POST.get("rating", "")
        review = request.POST.get("review", "")

        html = f"""
        <html>
        <head>
            <title>Review Added</title>
        </head>

        <body style="font-family:Arial;background:#f5f5f5">

            <h1>Posted Review</h1>

            <div style="
                background:#d1e7dd;
                padding:15px;
                margin:20px;
            ">
                <strong>Review successfully added!</strong>
            </div>

            <div style="
                background:white;
                padding:25px;
                margin:20px;
            ">
                <h2>{dealer["full_name"]}</h2>
                <p>Dealer ID: {dealer["id"]}</p>
                <p>City: {dealer["city"]}</p>
                <p>State: {dealer["state"]}</p>
                <p>Address: {dealer["address"]}</p>
            </div>

            <h2>Added Review</h2>

            <div style="
                background:white;
                padding:25px;
                margin:20px;
            ">
                <h3>{reviewer}</h3>
                <p><strong>Rating: {rating}/5</strong></p>
                <p>{review}</p>
            </div>

        </body>
        </html>
        """

        return HttpResponse(html)

    html = f"""
    <html>
    <head>
        <title>Post Review</title>
    </head>

    <body style="font-family:Arial;background:#f5f5f5">

        <h1>Post Review</h1>

        <div style="
            width:70%;
            margin:auto;
            background:white;
            padding:30px;
        ">

            <h2>{dealer["full_name"]}</h2>

            <form method="POST">

                <p>
                    <label>Dealer ID</label><br>
                    <input value="{dealer["id"]}" readonly>
                </p>

                <p>
                    <label>Your Name</label><br>
                    <input name="reviewer" required>
                </p>

                <p>
                    <label>Rating</label><br>
                    <select name="rating" required>
                        <option value="">Select Rating</option>
                        <option value="5">5 - Excellent</option>
                        <option value="4">4 - Very Good</option>
                        <option value="3">3 - Good</option>
                        <option value="2">2 - Fair</option>
                        <option value="1">1 - Poor</option>
                    </select>
                </p>

                <p>
                    <label>Review</label><br>
                    <textarea
                        name="review"
                        rows="5"
                        cols="60"
                        required
                    ></textarea>
                </p>

                <button type="submit">
                    Submit Review
                </button>

            </form>

        </div>

    </body>
    </html>
    """

    return HttpResponse(html)