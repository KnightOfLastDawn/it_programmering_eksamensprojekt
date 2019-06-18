unit it_interface;

{$mode objfpc}{$H+}

interface

uses
 Classes, SysUtils, FileUtil, Forms, Controls, Graphics, Dialogs, StdCtrls,
  Menus, ExtCtrls, Buttons, Process, LCLType, ActnList;

type

  { TForm1 }

  TForm1 = class(TForm)
    Button1: TButton;
    Button2: TButton;
    Button3: TButton;
    Button4: TButton;
    Edit2: TEdit;
    Edit3: TEdit;
    Exit1: TButton;
    Edit1: TEdit;
    Label1: TLabel;
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure Button3Click(Sender: TObject);
    procedure Button4Click(Sender: TObject);
  private

  public

  end;
const
  C_FNAME = 'textfile.txt';
  Cnt: Integer = 1;
  Cnt_1: Integer =1;

var
  Form1: TForm1;
  tfOut: Textfile;
  RunProgram: TProcess;
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
  Edit1.Text:=Edit2.Text;
  Cnt_1:=StrToInt(Edit2.Text);
  Edit3.Text:=IntToStr(Cnt_1);
  AssignFile(tfOut,C_FNAME);
  rewrite(tfOut);
  Write(tfOut, Cnt_1);
  CloseFile(tfOut);
  RunProgram := TProcess.Create(nil);
  RunProgram.CommandLine := 'python3 ./bestemmelse_af_rod_med_textfil_og_graf_v1.py';
  RunProgram.Execute;
  RunProgram.Free;
end;

procedure TForm1.Button4Click(Sender: TObject);
begin

end;


end.

