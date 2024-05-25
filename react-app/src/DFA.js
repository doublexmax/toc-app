import React from "react";

const DFA = () => {
    return (
        <div className="DFA">
            <div className="row">
                <div className="col-4 text-center">
                    <div className="m-auto">States</div>
                    <table className="states text-center">
                        <thead className="text-center">
                            <tr>
                                <th className="m-auto">State</th>
                                <th className="m-auto">Accepting?</th>
                                <th className="m-auto"></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>3</td>
                                <td>4</td>
                                <td>-</td>
                            </tr>
                        </tbody>
                    </table>
                    <div>
                        <span className="">New State:</span>
                    </div>
                </div>
                <div className="col-4 text-center">
                    <div>Start</div>
                    <div className="dropdown">
                        <button className="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            Dropdown button
                        </button>
                        <div className="dropdown-menu">
                            <div className="dropdown-item">
                                3
                            </div>
                        </div>
                    </div>
                </div>
                <div className="col-4 text-center">
                    <div>Input Alphabet</div>
                    <div className="inputAlph">

                    </div>
                    <div className="addAlph mt-2">

                    </div>
                </div>
            </div>
            <div className="row">

            </div>
        </div>
    );
};

export default DFA;