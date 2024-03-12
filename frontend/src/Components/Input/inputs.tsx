import { Component, FormEvent } from "react";
import "./input.css"

class Input extends Component {
    props: {
        campo: string, type: string, internal: string,
        form: (arg1: string, arg2: string) => boolean,
        add_function: (arg1: string, arg2: (arg01: string) => void) => void,
        initial_text: string
    }
    
    state: { texto: string, cor: string };
    
    constructor(props: {
        campo: string,
        type: string,
        internal: string,
        form: (arg1: string, arg2: string) => boolean,
        add_function: (arg1: string, arg2: (arg01: string) => void) => void,
        initial_text: string
    }
    ) {
        super(props);
        this.props = props;
        this.state = {texto: props.initial_text, cor: 'normal'};
        this.onChange = this.onChange.bind(this);
        this.changeColor = this.changeColor.bind(this);
        this.setText = this.setText.bind(this);
    }

    onChange(event: FormEvent) {
        // This is ok because it surely have the type value
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        this.setState({ texto: (event.target as any).value });
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        if (!this.props.form(this.props.campo, (event.target as any).value)) {
            this.changeColor('altered')
        }
        else {
            this.changeColor('normal')
        }
    }

    setText(text: string) {
        //console.log("hat")
        this.setState({ texto: text });
    }

    changeColor(type: string) {
        if (type === 'normal' || type === 'altered') {
            this.setState({ cor: type });
        }
    }

    render() {
        //console.log("oi")
        this.props.add_function(this.props.campo.toLowerCase() + "Color", this.changeColor);
        this.props.add_function(this.props.campo.toLowerCase() + "Text", this.setText)
        return (
            <div className={this.props.internal + " div"}>
                <div className="divWrapWrap">
                    <label className={this.props.internal + "-span input-text"}>
                        {this.props.campo}
                        <input className={"input " + this.state.cor} type={this.props.type} id={this.props.campo}
                            value={this.state.texto} onChange={this.onChange} />
                    </label>
                </div>
            </div>
        );
    }
}
export default Input;