import React from "react";
import { Pie, Bar } from "react-chartjs-2";
import "./Form.css";
//import Data from "../data";

function Charts({ value, label }) {
  return (
    <div className="col-md-4 box">
      {console.log(value)}
      <Bar
        data={{
          labels: value,
          datasets: [
            {
              label: label,
              backgroundColor: "rgba(255,99,132,0.2)",
              borderColor: "rgba(255,99,132,1)",
              borderWidth: 1,
              hoverBackgroundColor: "rgba(255,99,132,0.4)",
              hoverBorderColor: "rgba(255,99,132,1)",
              data: [65, 59, 80, 81, 56, 55],
            },
          ],
        }}
      />
    </div>
  );
}

export default Charts;
