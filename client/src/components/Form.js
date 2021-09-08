import React from "react";
import Data from "../data";
import "./Form.css";

function Form() {
  return (
    <div className="container">
      <h3 className="text-center">
        Please fill this survey and help them in taking effective measures for
        their health
      </h3>
      <div className="row">
        <form action="" method="post">
          <label htmlFor="age">Select Your Age</label>
          <select name="age" id="age">
            {Data.age.map((age, index) => (
              <option value={age} key={index}>
                {age}
              </option>
            ))}
          </select>
          <label htmlFor="water_tds">Water TDS</label>
          <select name="water_tds" id="water_tds">
            {Data.water_tds.map((water_tds, index) => (
              <option value={water_tds} key={index}>
                {water_tds}
              </option>
            ))}
          </select>
          <label htmlFor="aqi">AQI</label>
          <select name="aqi" id="aqi">
            {Data.aqi.map((aqi, index) => (
              <option value={aqi} key={index}>
                {aqi}
              </option>
            ))}
          </select>
          <label htmlFor="distance_from_industry">Distance From Industry</label>
          <select name="distance_from_industry" id="distance_from_industry">
            {Data.distance_from_industry.map(
              (distance_from_industry, index) => (
                <option value={distance_from_industry} key={index}>
                  {distance_from_industry}
                </option>
              )
            )}
          </select>
          <label htmlFor="disease_type">Disease Type</label>
          <select name="disease_type" id="disease_type">
            {Data.disease_type.map((disease_type, index) => (
              <option value={disease_type} key={index}>
                {disease_type}
              </option>
            ))}
          </select>
          <label htmlFor="sleep_hours">Sleep Hours</label>
          <select name="sleep_hours" id="sleep_hours">
            {Data.sleep_hours.map((sleep_hours, index) => (
              <option value={sleep_hours} key={index}>
                {sleep_hours}
              </option>
            ))}
          </select>
          <label htmlFor="exercise_hours">Exercise Hours</label>
          <select name="exercise_hours" id="exercise_hours">
            {Data.exercise_hours.map((exercise_hours, index) => (
              <option value={exercise_hours} key={index}>
                {exercise_hours}
              </option>
            ))}
          </select>
          <label htmlFor="weight">Weight</label>
          <select name="weight" id="weight">
            {Data.weight.map((weight, index) => (
              <option value={weight} key={index}>
                {weight}
              </option>
            ))}
          </select>
          <label htmlFor="height">Height</label>
          <select name="height" id="height">
            {Data.height.map((height, index) => (
              <option value={height} key={index}>
                {height}
              </option>
            ))}
          </select>
          <button className="btn btn-primary">Submit</button>
        </form>
      </div>
    </div>
  );
}

export default Form;
