unit it_interface;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, FileUtil, Forms, Controls, Graphics, Dialogs, StdCtrls;

type

  { TForm1 }

  TForm1 = class(TForm)
    Button1: TButton;
    Button2: TButton;
    Button3: TButton;
    Edit2: TEdit;
    Exit1: TButton;
    Edit1: TEdit;
    Label1: TLabel;
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure Button3Click(Sender: TObject);
  private

  public

  end;
const
  C_FNAME = 'textfile.txt';
  Cnt: Integer = 1;

var
  Form1: TForm1;
  tfOut: Textfile;
  //UserString: string;

implementation

{$R *.lfm}

{ TForm1 }

procedure TForm1.Button1Click(Sender: TObject);
begin
   inc(Cnt);
   Edit1.Text:=IntToStr(Cnt);
end;

procedure TForm1.Button2Click(Sender: TObject);
begin
  Close;
end;

procedure TForm1.Button3Click(Sender: TObject);
begin
  AssignFile(tfOut,C_FNAME);
  rewrite(tfOut);
  Write(tfOut, Cnt);
  CloseFile(tfOut);
end;


end.

