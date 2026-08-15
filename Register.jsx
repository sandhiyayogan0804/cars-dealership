server/frontend/src/components/Register/Register.jsx

import React, { useState } from "react";

const Register = () => {
  const [user, setUser] = useState({
    username: "",
    firstName: "",
    lastName: "",
    email: "",
    password: "",
  });

  const handleChange = (event) => {
    const { name, value } = event.target;

    setUser({
      ...user,
      [name]: value,
    });
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    console.log("Registration details:", user);
  };

  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-6">

          <div className="card shadow">
            <div className="card-body">

              <h2 className="text-center mb-4">
                Sign Up
              </h2>

              <form onSubmit={handleSubmit}>

                <div className="mb-3">
                  <label className="form-label">
                    Username
                  </label>

                  <input
                    type="text"
                    className="form-control"
                    name="username"
                    value={user.username}
                    onChange={handleChange}
                    required
                  />
                </div>

                <div className="mb-3">
                  <label className="form-label">
                    First Name
                  </label>

                  <input
                    type="text"
                    className="form-control"
                    name="firstName"
                    value={user.firstName}
                    onChange={handleChange}
                    required
                  />
                </div>

                <div className="mb-3">
                  <label className="form-label">
                    Last Name
                  </label>

                  <input
                    type="text"
                    className="form-control"
                    name="lastName"
                    value={user.lastName}
                    onChange={handleChange}
                    required
                  />
                </div>

                <div className="mb-3">
                  <label className="form-label">
                    Email
                  </label>

                  <input
                    type="email"
                    className="form-control"
                    name="email"
                    value={user.email}
                    onChange={handleChange}
                    required
                  />
                </div>

                <div className="mb-3">
                  <label className="form-label">
                    Password
                  </label>

                  <input
                    type="password"
                    className="form-control"
                    name="password"
                    value={user.password}
                    onChange={handleChange}
                    required
                  />
                </div>

                <button
                  type="submit"
                  className="btn btn-primary w-100"
                >
                  Register
                </button>

              </form>

            </div>
          </div>

        </div>
      </div>
    </div>
  );
};

export default Register;
