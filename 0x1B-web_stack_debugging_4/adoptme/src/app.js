const Pet = ({name, animal, breed}) => {
  return React.createElement("div", {}, [
    React.createElement("h1", {}, name),
    React.createElement("h2", {}, animal),
    React.createElement("h2", {}, breed),
  ]);
};

const App = () => {
  return React.createElement(
    "div",
    {id: "Dogs"},
    [
      React.createElement("h1", {}, "Adopt me!"),
      React.createElement(Pet, {name: "Polo", animal: "Dog", breed: "Pomeranian"}),
      React.createElement(Pet, {name: "Lola", animal: "Dog", breed: "Pincher"}),
      React.createElement(Pet, {name: "Lupe", animal: "Dog", breed: "Chihuaha"})
    ]);
};

ReactDOM.render(
  React.createElement(App),
  document.getElementById("root")
);