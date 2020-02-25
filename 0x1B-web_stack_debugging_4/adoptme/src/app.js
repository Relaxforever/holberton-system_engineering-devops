const Pet = () => {
  return React.createElement("div", {}, [
    React.createElement("h1", {}, "Polo"),
    React.createElement("h1", {}, "Dog"),
    React.createElement("h1", {}, "Pomenarian"),
  ]);
};

const App = () => {
  return React.createElement(
    "div",
    {id: "Dogos"},
    [
      React.createElement("h1", {}, "Adopt me!"),
      React.createElement(Pet),
      React.createElement(Pet),
      React.createElement(Pet)
    ]);
};

ReactDOM.render(
  React.createElement(App),
  document.getElementById("root")
);