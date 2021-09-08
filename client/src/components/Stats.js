import React from "react";
import Charts from "./Charts";
import { TezosToolkit } from "@taquito/taquito";
import { BeaconWallet } from "@taquito/beacon-wallet";
import Data from "../data";
import "./Form.css";
/*
const Tezos = new TezosToolkit("https://granadanet.smartpy.io");
const wallet = new BeaconWallet({ name: "Know Your Health" });

Tezos.setWalletProvider(wallet);

try {
  console.log("Requesting permissions...");
  const permissions = await wallet.client.requestPermissions();
  console.log("Got permissions:", permissions.address);
} catch (error) {
  console.log("Got error:", error);
}

const activeAccount = await wallet.client.getActiveAccount();
if (activeAccount) {
  // User already has account connected, everything is ready
  // You can now do an operation request, sign request, or send another permission request to switch wallet
  console.log("Already connected:", activeAccount.address);
  //return activeAccount;
} else {
  // The user is not connected. A button should be displayed where the user can connect to his wallet.
  console.log("Not connected!");
}

//let myAddress: string | undefined;

// Check if we are connected. If not, do a permission request first.
const activeAccount = await wallet.client.getActiveAccount();
if (!activeAccount) {
  const permissions = await wallet.client.requestPermissions();
  console.log("New connection:", permissions.address);
  myAddress = permissions.address;
} else {
  myAddress = activeAccount.address;
}

// At this point we are connected to an account.
// Let's send a simple transaction to the wallet that sends 1 mutez to ourselves.
const response = await wallet.sendOperations([
  {
    kind: TezosOperationType.TRANSACTION,
    destination: myAddress, // Send to ourselves
    amount: "1", // Amount in mutez, the smallest unit in Tezos
  },
]);

const blockHead = await Tezos.rpc.getBlock();

const contract = await Tezos.wallet.at(KT1HWdCPguqFT4SaghUns3S3VXYg1Qm8gZBc);
*/
function Stats() {
  return (
    <div className="container stats">
      <h3 className="text-center">Check What is Others Health</h3>
      <div className="row">
        <Charts value={Data.age} label="Age" />
        <Charts value={Data.water_tds} label="Water TDS" />
        <Charts value={Data.aqi} label="AQI" />
        <Charts
          value={Data.distance_from_industry}
          label="Distance From Industry"
        />
        <Charts value={Data.disease_type} label="Disease Type" />
        <Charts value={Data.sleep_hours} label="Sleep Hours" />
        <Charts value={Data.exercise_hours} label="Exercise Hours" />
        <Charts value={Data.weight} label="Weight" />
        <Charts value={Data.height} label="Height" />
      </div>
    </div>
  );
}

export default Stats;
